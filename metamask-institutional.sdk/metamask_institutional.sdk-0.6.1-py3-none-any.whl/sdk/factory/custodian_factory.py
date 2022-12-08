
from metamask_institutional.sdk.common.custodian import Custodian
from metamask_institutional.sdk.factory.custodian_name_to_client_adapter import CUSTODIAN_NAME_TO_CLIENT_ADAPTER
from metamask_institutional.sdk.mmiconfig.mmiconfig_client import MMIConfigClient


class CustodianFactory:
    """Utility class to instantiate custodians."""

    def __init__(self) -> None:
        mmiconfig_client = MMIConfigClient()
        self.custodians_config = mmiconfig_client.get_merged_custodian_configs()

    def get_supported_custodians(self):
        """Lists the names of custodians supported by the library. Use this name in the method "create_for" to instantiate a custodian object.

        Returns:
            The names of supported custodians, as a list of strings
        """
        return list(map(lambda config: config.name, self.custodians_config))

    def create_for(self, custodian_name: str, token: str) -> Custodian:
        """Creates an custodian instance for the passed custodian name.

        Args:
            custodian_name: The custodian name. Call the method "get_supported_custodians" to check the avaialble values.
            token: A token provided to you by the custodian. Depending on the custodian, it could be either a refresh token
            or an access token. Regardless of which, the library takes care of the authentication flow.

        Returns:
            The custodian instance.
        """
        configs_with_name = list(filter(
            lambda config: config.name == custodian_name, self.custodians_config))

        assert len(
            configs_with_name) > 0, f"Could not find a custodian with name {custodian_name}"

        config = configs_with_name[0]

        # Instantiate the client
        key = custodian_name if custodian_name in CUSTODIAN_NAME_TO_CLIENT_ADAPTER else "default"
        client_class = CUSTODIAN_NAME_TO_CLIENT_ADAPTER[key]["client"]
        adapter_class = CUSTODIAN_NAME_TO_CLIENT_ADAPTER[key]["adapter"]

        if config.refreshTokenUrl is not None:
            client = client_class(config.apiBaseUrl, token, config.refreshTokenUrl)
        else:
            client = client_class(config.apiBaseUrl, token)

        # Adapt the client into the class Custodian
        return adapter_class(client)
