import json
import pickle
from json import JSONDecodeError
from typing import Type, Callable, NoReturn

from fhirpy.base.exceptions import ResourceNotFound, OperationOutcome, InvalidResponse
from fhirpy.base.utils import (
    AttrDict,
    unique_everseen,
)
from fhirpy.lib import AsyncFHIRClient, AsyncFHIRSearchSet
from loguru import logger
from seito.monad.async_opt import aopt
from tenacity import retry, stop_after_attempt, retry_if_exception_type

from smart_on_fhir_client.partner import Partner, Organization, TokenEndpointResponse
from smart_on_fhir_client.requester.fhir_resource import CustomFHIRResource
from smart_on_fhir_client.session import session_manager
from smart_on_fhir_client.strategy import Strategy


class UnauthorizedError(Exception):
    ...


# @mixin
# class RefreshTokenHandlerMixin:
#     async def trade_refresh_token_to_access_token(self) -> tuple[str, str] | NoReturn:
#         try:
#             (
#                 access_token,
#                 refresh_token,
#             ) = await self.partner.trade_refresh_for_access_token(self.refresh_token)
#         except Exception as e:
#             logger.error(e)
#             raise e
#         else:
#             return access_token, refresh_token


class CustomFHIRSearchSet(AsyncFHIRSearchSet):
    """
    custom fhir search with post
    """

    async def fetch(self, all_resources: bool = False):
        """
        Add a new parameters to get all resources (got only the type)
        Args:
            all_resources: boolean

        Returns:

        """
        # noinspection PyProtectedMember
        bundle_data = await self.client._fetch_resource(self.resource_type, self.params)
        resources = self._get_bundle_resources(bundle_data, all_resources)
        return resources

    async def post_fetch(self, enable_modifier=False):
        def _check_modifier(val: str):
            if enable_modifier:
                return val
            # try to remove modifier
            val_parts = val.split(":")
            return val_parts[0]

        params = {
            _check_modifier(k): ",".join(
                map(str, unique_everseen(v)) if isinstance(v, list) else [str(v)]
            )
            for k, v in self.params.items()
        }

        # noinspection PyProtectedMember
        bundle_data = await self.client._do_request(
            "POST", path=f"{self.resource_type}/_search", data=params, form_encoded=True
        )
        resources = self._get_bundle_resources(bundle_data)
        return resources

    async def post_first(self, enable_modifier: bool = False):
        result = await self.post_fetch(enable_modifier=enable_modifier)
        return result[0] if result else None

    def _get_bundle_resources(self, bundle_data, all_resources: bool = False):
        bundle_resource_type = bundle_data.get("resourceType", None)

        if bundle_resource_type != "Bundle":
            raise InvalidResponse(
                "Expected to receive Bundle "
                "but {0} received".format(bundle_resource_type)
            )

        resources_data = [res["resource"] for res in bundle_data.get("entry", [])]

        resources = []
        for data in resources_data:
            resource = self._perform_resource(data)
            if all_resources or resource.resource_type == self.resource_type:
                resources.append(resource)
        return resources


class SmartOnFhirClient(AsyncFHIRClient):
    """
    Simply overrides the _do_request methods to perform exponential backoff
    and retries
    """

    searchset_class = CustomFHIRSearchSet

    def __init__(
        self,
        url,
        authorization=None,
        extra_headers=None,
        refresh_token: str | None = None,
        partner: Partner = None,
        fhir_manager=None,
        strategy=None,
        organization=None,
    ):
        super(AsyncFHIRClient, self).__init__(url, authorization, extra_headers)
        self.refresh_token = refresh_token
        self.partner = partner
        self.fhir_manager = fhir_manager
        self.strategy = strategy
        self.organization = organization

    @property
    def client_name(self):
        return (
            self.organization.slug
            if self.organization is not None
            else self.partner_name
        )

    @property
    def partner_name(self):
        return self.partner.name

    @retry(stop=stop_after_attempt(3), retry=retry_if_exception_type(UnauthorizedError))
    async def _retry(self, method, path, data=None, params=None, form_encoded=False):
        # if we do not have an authorization token
        # try fetch one
        if not self.authorization:
            await self.fetch_access_token()

        headers = self._build_request_headers()
        url = self._build_request_url(path, params)
        logger.debug("Fetching {}", url)

        body = dict(data=data) if form_encoded else dict(json=data)

        async with session_manager.fhir_client_session.request(
            method, url, headers=headers, **body
        ) as r:
            if 200 <= r.status < 300:
                data = await r.text()
                return json.loads(data, object_hook=AttrDict)

            if r.status == 404 or r.status == 410:
                raise ResourceNotFound(await r.text())

            if r.status == 403 or r.status == 401:
                # retry with a refresh token
                # fetch a brand-new access token ?
                await self.fetch_access_token()
                # self.trade_refresh_token_to_access_token()
                # self.authorization = f"Bearer {access}"
                # self.refresh_token = refresh
                raise UnauthorizedError("Retrying because of unauthorized")

            data = await r.text()
            try:
                parsed_data = json.loads(data)
                if parsed_data["resourceType"] == "OperationOutcome":
                    raise OperationOutcome(resource=parsed_data)
                raise OperationOutcome(reason=data)
            except (KeyError, JSONDecodeError):
                raise OperationOutcome(reason=data)

    async def _do_request(
        self, method, path, data=None, params=None, form_encoded=False
    ):
        return await self._retry(
            method, path, data=data, params=params, form_encoded=form_encoded
        )

    async def fetch_access_token(self):
        if self.refresh_token is not None:
            try:
                (
                    access_token,
                    refresh_token,
                ) = await self.partner.trade_refresh_token_for_access_token(
                    self.refresh_token
                )
                self.refresh_token = refresh_token
                self.authorization = f"Bearer {access_token}"
                return
            except Exception as e:
                logger.error(e)
                logger.warning(f"Unable to fetch access token for {self.client_name=}")
                raise UnauthorizedError("Can not get access token")

        logger.debug(f"Trying to fetch access token for {self.client_name=}")
        try:
            access_token = await self.partner.get_access_token_for_strategy(
                self.strategy,
                **(
                    self.organization.parameters
                    if self.organization is not None
                    else {}
                ),
            )
        except Exception as e:
            logger.error(e)
            logger.warning(f"Unable to fetch access token for {self.client_name=}")
            raise UnauthorizedError("Can not get access token")
        else:
            self.authorization = f"Bearer {access_token}"

    def resource(self, resource_type: str = None, **kwargs):
        if resource_type is None:
            raise TypeError("Argument `resource_type` is required")

        wanted_cls = self.fhir_manager.cls_by_partner_id[self.client_name].get(
            resource_type
        )
        cls = wanted_cls or CustomFHIRResource
        return cls(self, resource_type=resource_type, **kwargs)

    def dumps(self):
        return pickle.dumps(self)

    def __str__(self):
        return f"< SmartOnFhirClient url={self.url} >"


class InvalidAccessToken(Exception):
    ...


class SmartOnFhirClientBuilder:
    def __init__(self):
        """ """
        self._partner: Partner | None = None
        self._strategy: Strategy | None = None
        self._organization: Organization | None = None
        self._session = session_manager.fhir_client_session
        self._cls_by_resource = {}
        self._target_fhir_server_authorization: str | Callable[..., str] | None = None

    @property
    def partner(self):
        return self._partner

    @property
    def strategy(self):
        return self._strategy

    @property
    def organization(self):
        return self._organization

    @property
    def cls_by_resource(self):
        return self._cls_by_resource

    @property
    def target_fhir_server_authorization(self):
        return self._target_fhir_server_authorization

    def _check_partner(self) -> NoReturn:
        """ """
        if not self._partner:
            raise ValueError("No partner registered")

    def for_partner(self, client: Partner) -> "SmartOnFhirClientBuilder":
        """

        Args:
            client:

        Returns:

        """
        self._partner = client
        return self

    def for_strategy(self, strategy: Strategy) -> "SmartOnFhirClientBuilder":
        """

        Args:
            strategy:

        Returns:

        """
        self._check_partner()
        self._strategy = strategy
        return self

    def for_organization(
        self, organization: Organization
    ) -> "SmartOnFhirClientBuilder":
        """

        Args:
            organization:

        Returns:

        """
        self._check_partner()
        self._organization = organization
        return self

    for_practitioner = for_organization

    def register_cls_for(
        self, resource: str, cls: Type[CustomFHIRResource]
    ) -> "SmartOnFhirClientBuilder":
        """

        Args:
            resource:
            cls:

        Returns:

        """
        self._check_partner()
        self._cls_by_resource[resource] = cls
        return self

    def register_target_server_authorization(
        self, jwt_token: str | Callable[..., str]
    ) -> "SmartOnFhirClientBuilder":
        """

        Args:
            jwt_token:

        Returns:

        """
        self._check_partner()
        self._target_fhir_server_authorization = jwt_token
        return self

    async def build(self, fhir_manager) -> SmartOnFhirClient:
        """
        build asynchronously a fhir client
        """

        def build_client(
            token_endpoint_response: TokenEndpointResponse,
        ):  # access_token: str, refresh_token: str = None):
            access_token = token_endpoint_response.access_token
            if access_token:
                organization = (
                    self._organization.slug if self._organization else "No organization"
                )
                logger.info(
                    f"Successfully initialized {self._partner.name=} {organization=} client ! "
                )
            else:
                logger.warning(
                    f"Unable to initialize {self._partner.name=} client...A retry will be performed at first call"
                )
            return SmartOnFhirClient(
                self._partner.fhir_url,
                authorization=f"Bearer {access_token}" if access_token else "",
                refresh_token=token_endpoint_response.refresh_token,
                partner=self._partner,
                fhir_manager=fhir_manager,
                strategy=self._strategy,
                organization=self._organization,
            )

        return await (
            aopt(
                self._partner.get_access_token_for_strategy,
                self._strategy,
                **(
                    self._organization.parameters
                    if self._organization is not None
                    else {}
                ),
            )
            .map(build_client)
            .or_else(lambda: build_client(TokenEndpointResponse()))
        )


# noinspection PyPep8Naming
class smart_on_fhir_client:
    """ """

    @staticmethod
    def builder() -> SmartOnFhirClientBuilder:
        """

        Returns:

        """
        return SmartOnFhirClientBuilder()
