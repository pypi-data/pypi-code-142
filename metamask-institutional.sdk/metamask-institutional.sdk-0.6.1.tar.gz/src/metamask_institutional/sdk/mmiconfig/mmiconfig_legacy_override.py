"""
Override configs for legacy custodians.
The MMI configuration API doesn't provide the actual configs for legacy custodians,
so we deffine overrides in the list.
"""

from metamask_institutional.sdk.mmiconfig.mmi_config import MMIConfig

overrides = {
    "custodians": [
        {
            "name": "qredo",
            "apiBaseUrl": "https://api.qredo.network",
            "refreshTokenUrl": None,
        },
        {
            "name": "qredo-dev",
            "apiBaseUrl": "https://7ba211-api.qredo.net",
            "refreshTokenUrl": None,
        },
        {
            "name": "cactus",
            "apiBaseUrl": "https://api.mycactus.com/custody/v1/mmi-api",
            "refreshTokenUrl": None,
        },
        {
            "name": "cactus-dev",
            "apiBaseUrl": "https://api.mycactus.dev/custody/v1/mmi-api",
            "refreshTokenUrl": None,
        },
        {
            "name": "bitgo",
            "apiBaseUrl": "https://app.bitgo.com/defi/v1/mmi",
            "refreshTokenUrl": None,
        },
        {
            "name": "bitgo-test",
            "apiBaseUrl": "https://app.bitgo-test.com/defi/v1/mmi",
            "refreshTokenUrl": None,
        }
    ]
}

MMICONFIG_LEGACY_OVERRIDE = MMIConfig(**overrides)
