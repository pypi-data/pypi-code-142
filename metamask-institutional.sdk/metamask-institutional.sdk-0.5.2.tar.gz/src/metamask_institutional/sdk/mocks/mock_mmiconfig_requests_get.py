from metamask_institutional.sdk.mocks.mock_mmiconfig_dev import MOCK_MMICONFIG_DEV
from metamask_institutional.sdk.mocks.mock_mmiconfig_prod import MOCK_MMICONFIG_PROD
from metamask_institutional.sdk.mocks.mock_response import MockResponse


def mock_mmiconfig_requests_get(*args, **kwargs):
    """ This method will be used by the mock to replace requests.get"""

    if args[0].__contains__('prod'):
        return MockResponse(MOCK_MMICONFIG_PROD, 200)

    return MockResponse(MOCK_MMICONFIG_DEV, 200)
