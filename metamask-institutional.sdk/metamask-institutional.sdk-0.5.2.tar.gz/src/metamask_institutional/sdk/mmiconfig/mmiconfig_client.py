
from typing import List

import requests
from pydantic import HttpUrl

from metamask_institutional.sdk.mmiconfig.custodian_config import CustodianConfig
from metamask_institutional.sdk.mmiconfig.mmi_config import MMIConfig
from metamask_institutional.sdk.mmiconfig.mmiconfig_legacy_override import MMICONFIG_LEGACY_OVERRIDE

MMI_CONFIGURATION_API_DEV = "https://mmi-configuration-api.codefi.network/v1/configuration/default"
MMI_CONFIGURATION_API_PROD = "https://mmi-configuration-api.mmi-prod.codefi.network/v1/configuration/default"


class MMIConfigClient():

    def __get_mmi_config(self, api_url: HttpUrl) -> MMIConfig:
        response = requests.get(api_url, timeout=1)

        if response.status_code != 200:
            raise requests.HTTPError(
                f'Could not fetch the MMI Configuration in dev. Request failed with code {response.status_code}, {response.text}.')

        return MMIConfig(**response.json())

    def get_merged_custodian_configs(self) -> List[CustodianConfig]:
        """
        Fetch custodian configurations from the MMI configuration API in dev, in prod.
        Then apply the overrides for the legacy custodians.

        Returns the merged list of custodian configs.
        """
        mmi_config_dev = self.__get_mmi_config(MMI_CONFIGURATION_API_DEV)
        mmi_config_prod = self.__get_mmi_config(MMI_CONFIGURATION_API_PROD)
        custodians_config_dev = mmi_config_dev.custodians
        custodians_config_prod = mmi_config_prod.custodians
        custodians_config_legacy = MMICONFIG_LEGACY_OVERRIDE.custodians

        legacy_custodian_names = list(map(lambda config: config.name, custodians_config_legacy))

        # Remove the configs for legacy custodians. We override them with harcoded values
        custodians_config_dev_cleaned = list(filter(lambda config: config.name not in legacy_custodian_names, custodians_config_dev))
        custodians_config_prod_cleaned = list(filter(lambda config: config.name not in legacy_custodian_names, custodians_config_prod))

        return custodians_config_dev_cleaned + custodians_config_prod_cleaned + custodians_config_legacy
