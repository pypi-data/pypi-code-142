from __future__ import annotations

import base64
import enum
import json
import logging
import time
from concurrent.futures import Future, ThreadPoolExecutor
from datetime import datetime
from itertools import chain
from typing import Any, Iterable, Iterator, List, Mapping, Optional, Sequence, Type, TypeVar, Union
from urllib.parse import urljoin

import polars as pl
import requests
from pydantic import BaseModel, ValidationError
from requests import HTTPError

from chalk.client.client_protocol import (
    ChalkAPIClientProtocol,
    ChalkBaseException,
    ChalkError,
    FeatureResult,
    OfflineQueryContext,
    OnlineQueryContext,
    OnlineQueryResponse,
    ResolverRunResponse,
    WhoAmIResponse,
)
from chalk.config.auth_config import load_token
from chalk.features import DataFrame, Feature, Features, FeatureWrapper, unwrap_feature
from chalk.features.pseudofeatures import CHALK_TS_FEATURE
from chalk.serialization.codec import FEATURE_CODEC

_logger = logging.getLogger(__name__)

import pandas as pd


class _ExchangeCredentialsRequest(BaseModel):
    client_id: str
    client_secret: str
    grant_type: str


class _ExchangeCredentialsResponse(BaseModel):
    access_token: str
    token_type: str
    expires_in: int
    engines: Optional[Mapping[str, str]] = None


class _OfflineQueryResponse(BaseModel):
    columns: List[str]
    output: List[List[Any]]
    errors: Optional[List[ChalkError]]


class _OfflineQueryInput(BaseModel):
    columns: List[str]
    values: List[List[Any]]


class _OfflineQueryRequest(BaseModel):
    output: List[str]
    input: Optional[_OfflineQueryInput] = None
    dataset: Optional[str] = None
    max_samples: Optional[int] = None


class _QueryRequest(BaseModel):
    inputs: Mapping[str, Any]
    outputs: List[str]
    staleness: Optional[Mapping[str, str]] = None
    context: Optional[OnlineQueryContext]
    deployment_id: Optional[str] = None
    correlation_id: Optional[str] = None
    query_name: Optional[str] = None
    meta: Optional[Mapping[str, str]] = None


class _TriggerResolverRunRequest(BaseModel):
    resolver_fqn: str


class _GetRunStatusRequest(BaseModel):
    run_id: str


T = TypeVar("T")


class _ChalkClientConfig(BaseModel):
    client_id: str
    client_secret: str
    api_server: str
    active_environment: Optional[str]


class _OnlineQueryResponse(BaseModel):
    data: List[FeatureResult]
    errors: Optional[List[ChalkError]]


class _DatasetErrorResponse(BaseModel):
    fatal_errors: List[ChalkError]


class _CreateOfflineQueryJobRequest(BaseModel):
    """
    Attributes
        output: A list of output feature root fqns to query
        destination_format: The desired output format. Should be 'CSV' or 'PARQUET'
        input: Any givens
        max_samples: The maximum number of samples
    """

    output: List[str]
    destination_format: str
    input: Optional[_OfflineQueryInput] = None
    max_samples: Optional[int] = None
    observed_at_lower_bound: Optional[datetime] = None
    observed_at_upper_bound: Optional[datetime] = None
    dataset_name: Optional[str] = None
    branch: Optional[str] = None
    environment: Optional[str] = None


class _CreateOfflineQueryJobResponse(BaseModel):
    """
    Attributes:
        job_id: A job ID, which can be used to retrieve the results.
    """

    job_id: str
    version: int = 1  # Deprecated
    errors: Optional[List[ChalkError]]


class _GetOfflineQueryJobResponse(BaseModel):
    """
    Attributes:
        is_finished: Whether the export job is finished (it runs asynchronously)
        signed_urls: A list of signed URLs that the client can download to retrieve the exported data.
    """

    is_finished: bool
    urls: List[str]


class ChalkConfigurationException(ChalkBaseException):
    message: str

    def __init__(self, message: str):
        super().__init__(message)

    @classmethod
    def missing_dependency(cls, name: str):
        return cls(f"Missing pip dependency '{name}'. Please add this to your requirements.txt file and pip install.")


class ChalkOfflineQueryException(ChalkBaseException):
    message: str
    errors: List[ChalkError]

    def __init__(self, message: str, errors: List[ChalkError]):
        self.message = message
        self.errors = errors
        super().__init__(message + "\n" + "\n".join(["\t" + e.message for e in errors[0:3]]))


class ChalkResolverRunException(ChalkBaseException):
    message: str

    def __init__(self, message: str):
        self.message = message
        super().__init__(message)


class ChalkDatasetDownloadException(ChalkBaseException):
    message: str

    def __init__(self, message: str):
        self.message = message
        super().__init__(message)


class OnlineQueryResponseWrapper(OnlineQueryResponse):
    data: List[FeatureResult]
    errors: Optional[List[ChalkError]]

    def __init__(
        self,
        data: List[FeatureResult],
        errors: Optional[List[ChalkError]],
    ):
        self.data = data
        self.errors = errors
        for d in self.data:
            if d.value is not None:
                d.value = FEATURE_CODEC.decode_fqn(d.field, d.value)
        self._values = {d.field: d for d in self.data}

    def get_feature(self, feature: Any) -> Optional[FeatureResult]:
        # Typing `feature` as Any, as the Features will be typed as the underlying datatypes, not as Feature
        return self._values.get(_get_feature_root_fqn(feature))

    def get_feature_value(self, feature: Any) -> Optional[Any]:
        # Typing `feature` as Any, as the Features will be typed as the underlying datatypes, not as Feature
        v = self.get_feature(feature)
        return v and v.value


def _get_feature_root_fqn(feat: Union[str, Feature, FeatureWrapper, Any]) -> str:
    if isinstance(feat, str):
        return feat
    elif isinstance(feat, FeatureWrapper):
        return unwrap_feature(feat).root_fqn
    elif isinstance(feat, Feature):
        return feat.root_fqn
    raise ValueError(f"Reference must be to a leaf feature. Received '{feat}'")


def _expand_scalar_features_shallow(fs: Sequence[Any]) -> Iterator[str]:
    for o in fs:
        if isinstance(o, str):
            yield o
        if isinstance(o, type) and issubclass(o, Features):
            for f in o.features:
                if f.is_scalar:
                    yield f.root_fqn
        if isinstance(o, FeatureWrapper):
            o = unwrap_feature(o)

        if isinstance(o, Feature) and o.is_scalar:
            yield o.root_fqn
        elif isinstance(o, Feature) and o.is_has_one:
            assert o.joined_class is not None
            for f in o.joined_class.features:
                if isinstance(f, Feature) and f.is_scalar:
                    yield f"{o.root_fqn}.{f.name}"


class ChalkAPIClientImpl(ChalkAPIClientProtocol):
    def __init__(
        self,
        *,
        client_id: Optional[str],
        client_secret: Optional[str],
        environment: Optional[str],
        api_server: Optional[str],
    ):
        if client_id is not None and client_secret is not None:
            self._config = _ChalkClientConfig(
                client_id=client_id,
                client_secret=client_secret,
                api_server=api_server or "https://api.chalk.ai",
                active_environment=environment,
            )
        else:
            token = load_token()
            if token is None:
                raise ValueError(
                    (
                        "Could not find .chalk.yml config file for project, "
                        "and explicit configuration was not provided. "
                        "You may need to run `chalk login` from your command line, "
                        "or check that your working directory is set to the root of "
                        "your project."
                    )
                )
            self._config = _ChalkClientConfig(
                client_id=token.clientId,
                client_secret=token.clientSecret,
                api_server=api_server or token.apiServer or "https://api.chalk.ai",
                active_environment=environment or token.activeEnvironment,
            )

        self._default_headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }
        self._engines: Optional[Mapping[str, str]] = None
        self._exchanged_credentials = False

    def _exchange_credentials(self):
        _logger.debug("Performing a credentials exchange")
        resp = requests.post(
            url=urljoin(self._config.api_server, f"v1/oauth/token"),
            headers={
                "Accept": "application/json",
                "Content-Type": "application/json",
            },
            json=_ExchangeCredentialsRequest(
                client_id=self._config.client_id,
                client_secret=self._config.client_secret,
                grant_type="client_credentials",
            ).dict(),
            timeout=10,
        )
        response_json = resp.json()
        try:
            creds = _ExchangeCredentialsResponse(**response_json)
        except ValidationError:
            raise HTTPError(response_json)
        self._default_headers["Authorization"] = f"Bearer {creds.access_token}"
        self._engines = creds.engines
        self._exchanged_credentials = True

    def _get_headers(self, environment_override: Optional[str]):
        x_chalk_env_id = environment_override or self._config.active_environment
        headers = dict(self._default_headers)  # shallow copy
        if x_chalk_env_id is not None:
            headers["X-Chalk-Env-Id"] = x_chalk_env_id
        return headers

    def _request(
        self,
        method: str,
        uri: str,
        response: Type[T],
        json: Optional[BaseModel] = None,
        use_engine: bool = False,
        environment_override: Optional[str] = None,
    ) -> T:
        # Track whether we already exchanged credentials for this request
        exchanged_credentials = False
        if not self._exchanged_credentials:
            exchanged_credentials = True
            self._exchange_credentials()
        headers = self._get_headers(environment_override=environment_override)
        active_env = environment_override or self._config.active_environment
        if use_engine and self._engines is not None and active_env in self._engines:
            assert isinstance(active_env, str)
            base = self._engines[active_env]
        else:
            base = self._config.api_server
        url = urljoin(base, uri)
        json_body = json and json.dict()
        r = requests.request(method=method, headers=headers, url=url, json=json_body)
        if r.status_code in (401, 403) and not exchanged_credentials:
            # It is possible that credentials expired, or that we changed permissions since we last
            # got a token. Exchange them and try again
            self._exchange_credentials()
            r = requests.request(method=method, headers=headers, url=url, json=json_body)

        r.raise_for_status()
        return response(**r.json())

    def whoami(self) -> WhoAmIResponse:
        return self._request(method="GET", uri=f"/v1/who-am-i", response=WhoAmIResponse)

    def upload_features(
        self,
        input: Mapping[Union[str, Feature, Any], Any],
        context: Optional[OnlineQueryContext] = None,
        preview_deployment_id: Optional[str] = None,
        correlation_id: Optional[str] = None,
        query_name: Optional[str] = None,
        meta: Optional[Mapping[str, str]] = None,
    ) -> Optional[List[ChalkError]]:
        return self.query(
            input=input,
            output=list(input.keys()),
            staleness=None,
            context=context,
            preview_deployment_id=preview_deployment_id,
            correlation_id=correlation_id,
            query_name=query_name,
            meta=meta,
        ).errors

    def query(
        self,
        input: Mapping[Union[str, Feature, FeatureWrapper, Any], Any],
        output: List[Union[str, Feature, Any]],
        staleness: Optional[Mapping[Union[str, Feature, Any], str]] = None,
        context: Optional[OnlineQueryContext] = None,
        preview_deployment_id: Optional[str] = None,
        correlation_id: Optional[str] = None,
        query_name: Optional[str] = None,
        meta: Optional[Mapping[str, str]] = None,
    ) -> OnlineQueryResponse:
        encoded_inputs = {}
        for feature, value in input.items():
            fqn = _get_feature_root_fqn(feature)
            encoded_inputs[fqn] = FEATURE_CODEC.encode_fqn(fqn, value)

        request = _QueryRequest(
            inputs=encoded_inputs,
            outputs=list(_expand_scalar_features_shallow(output)),
            staleness=staleness and {_get_feature_root_fqn(k): v for k, v in staleness.items()},
            context=context,
            deployment_id=preview_deployment_id,
            correlation_id=correlation_id,
            query_name=query_name,
            meta=meta,
        )

        resp = self._request(
            method="POST",
            uri="/v1/query/online",
            json=request,
            response=_OnlineQueryResponse,
            use_engine=preview_deployment_id is None,
            environment_override=context.environment if context else None,
        )
        return OnlineQueryResponseWrapper(
            data=resp.data,
            errors=resp.errors,
        )

    def get_training_dataframe(
        self,
        input: Union[Mapping[Union[str, Feature], Any], pl.DataFrame, pd.DataFrame, DataFrame],
        input_times: List[datetime],
        output: List[Union[str, Feature, Any]],
        context: Optional[OfflineQueryContext] = None,
        dataset: Optional[str] = None,
        branch: Optional[str] = None,
    ) -> pd.DataFrame:
        if not isinstance(input, DataFrame):
            input = DataFrame(input)

        self._get_headers(environment_override=None)

        return self._get_training_dataframe(
            input=input.to_pandas(),
            input_times=input_times,
            output=output,
            context=context,
            dataset=dataset,
            branch=branch,
        )

    def _decode_offline_response(self, offline_query_response: _OfflineQueryResponse) -> pd.DataFrame:
        data = {}
        for col_index, column in enumerate(offline_query_response.output):
            series_values = []
            for value in column:
                value = FEATURE_CODEC.decode_fqn(
                    fqn=offline_query_response.columns[col_index],
                    value=value,
                )
                if isinstance(value, enum.Enum):
                    value = value.value
                series_values.append(value)

            data[offline_query_response.columns[col_index]] = pd.Series(
                data=series_values,
                dtype=FEATURE_CODEC.get_pandas_dtype(offline_query_response.columns[col_index]),
            )
        return pd.DataFrame(data)

    def _get_training_dataframe(
        self,
        input: pd.DataFrame,
        input_times: List[datetime],
        output: List[Union[str, Feature, Any]],
        context: Optional[OfflineQueryContext] = None,
        dataset: Optional[str] = None,
        branch: Optional[str] = None,
    ) -> pd.DataFrame:
        columns = input.columns
        matrix = input.T.values.tolist()

        columns_fqn = [_get_feature_root_fqn(c) for c in chain(columns, (CHALK_TS_FEATURE,))]

        matrix.append([a for a in input_times])

        for col_index, column in enumerate(matrix):
            for row_index, value in enumerate(column):
                matrix[col_index][row_index] = FEATURE_CODEC.encode_fqn(
                    fqn=columns_fqn[col_index],
                    value=value,
                )

        query_input = _OfflineQueryInput(
            columns=columns_fqn,
            values=matrix,
        )

        query_output = list(_expand_scalar_features_shallow(output))

        try:
            response = self._create_and_await_offline_query_job(
                output=query_output,
                input=query_input,
                dataset_name=dataset,
                branch=branch,
                environment=context and context.environment,
            )
            return response.to_pandas()
        except HTTPError as e:
            _logger.debug("Got HTTP Exception while processing sample query", exc_info=e)
            raise ChalkOfflineQueryException(message=f"HTTP error while processing sample query.", errors=[])

    def sample(
        self,
        output: List[Union[str, Feature, Any]],
        max_samples: Optional[int] = None,
        context: Optional[OfflineQueryContext] = None,
    ) -> pd.DataFrame:
        query_output = _expand_scalar_features_shallow(output)

        try:
            response = self._create_and_await_offline_query_job(output=query_output, max_samples=max_samples)
        except HTTPError as e:
            _logger.debug("Got HTTP Exception while processing sample query", exc_info=e)
            raise ChalkOfflineQueryException(message=f"HTTP error while processing sample query.", errors=[])

        return response.to_pandas()

    def trigger_resolver_run(
        self,
        resolver_fqn: str,
        deployment_id: Optional[str] = None,
    ) -> ResolverRunResponse:
        _logger.debug(f'Triggering resolver {resolver_fqn} to run with deployment ID "{deployment_id}"')

        request = _TriggerResolverRunRequest(resolver_fqn=resolver_fqn)
        try:
            response = self._request(
                method="POST",
                uri="/v1/runs/trigger",
                json=request,
                response=ResolverRunResponse,
            )
        except HTTPError as e:
            message = str(e)

            detail = e.response.json().get("detail")
            if detail is not None:
                message = detail

            raise ChalkResolverRunException(message=message)

        return response

    def get_run_status(self, run_id: str) -> ResolverRunResponse:
        try:
            response = self._request(
                method="GET",
                uri=f"/v1/runs/{run_id}",
                response=ResolverRunResponse,
            )
        except HTTPError as e:
            message = str(e)

            detail = e.response.json().get("detail")
            if detail is not None:
                message = detail

            raise ChalkResolverRunException(message=message)

        return response

    def _decode_col_name(self, col_name: str) -> str:
        x_split = col_name.split("_")
        if x_split[0] == "ca":
            assert len(x_split) == 2
            return x_split[1]
        elif x_split[0] == "cb":
            root_fqn_b32 = x_split[1]
            return base64.b32decode(root_fqn_b32.replace("0", "=").upper()).decode("utf8") + "_".join(x_split[2:])
        else:
            raise ValueError(f"Unexpected identifier: {x_split[0]}")

    def _decode_column_names(self, column_names: List[str], ts_fqn: Optional[str]) -> Mapping[str, str]:
        ans: Mapping[str, str] = {}
        for x in column_names:
            if x.endswith("__"):
                if x == "__observed_at__" and ts_fqn is not None:
                    ans[x] = ts_fqn
                continue
            ans[x] = self._decode_col_name("_".join(x.split("_")[:2]))
        return ans

    def _create_and_await_offline_query_job(
        self,
        output: Iterable[str],
        input: Optional[_OfflineQueryInput] = None,
        max_samples: Optional[int] = None,
        dataset_name: Optional[str] = None,
        branch: Optional[str] = None,
        environment: Optional[str] = None,
    ) -> pl.DataFrame:
        output = list(output)
        req = _CreateOfflineQueryJobRequest(
            output=output,
            destination_format="PARQUET",
            input=input,
            max_samples=max_samples,
            dataset_name=dataset_name,
            branch=branch,
            environment=environment,
        )
        response = self._create_offline_query_job(request=req)

        if response.errors is not None and len(response.errors) > 0:
            raise ChalkOfflineQueryException(message="Failed to execute offline query", errors=response.errors)

        while True:
            status = self._get_job_status(job_id=response.job_id)
            if status.is_finished:
                break
            time.sleep(0.5)

        executor = ThreadPoolExecutor(max_workers=16)

        df_futures: list[Future[pl.DataFrame]] = []
        for f in status.urls:
            df_futures.append(executor.submit(pl.read_parquet, f))

        dfs = [df.result() for df in df_futures]

        # dfs: List[pl.DataFrame] = await asyncio.gather(*get_df_futs)
        dfs = [x.select(sorted(x.columns)) for x in dfs]
        df = pl.concat(dfs)

        ts_fqn = next((f for f in output if Feature.from_root_fqn(f).is_feature_time), None)
        decoded_col_names = self._decode_column_names(
            df.columns,
            ts_fqn=None,
        )
        df = df.select(list(decoded_col_names.keys()))
        df = df.rename(dict(decoded_col_names))
        # The parquet file is all encoded. We gotta decode
        decoded_stmts = []
        for col in df.columns:
            if col == ts_fqn or col == CHALK_TS_FEATURE.root_fqn:
                decoded_stmts.append(pl.col(col).dt.with_time_zone("UTC"))
            else:

                def _bound_decode(val: Any, col: str = col):
                    if val is None:
                        return None
                    return json.loads(val)

                decoded_stmts.append(
                    pl.col(col).apply(_bound_decode, return_dtype=FEATURE_CODEC.get_polars_dtype(fqn=col))
                )

        df = df.select(decoded_stmts)
        return df.select(sorted(df.columns))

    def _create_offline_query_job(self, request: _CreateOfflineQueryJobRequest):
        response = self._request(
            method="POST", uri="/v2/offline_query", json=request, response=_CreateOfflineQueryJobResponse
        )
        return response

    def _get_job_status(self, job_id: str) -> _GetOfflineQueryJobResponse:
        return self._request(method="GET", uri=f"/v2/offline_query/{job_id}", response=_GetOfflineQueryJobResponse)
