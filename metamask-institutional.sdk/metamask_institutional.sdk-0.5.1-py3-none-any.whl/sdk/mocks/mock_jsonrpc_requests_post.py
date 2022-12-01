from metamask_institutional.sdk.mocks.mock_jsonrpc_create_tx_response import MOCK_JSONRPC_CREATE_TX_RESPONSE
from metamask_institutional.sdk.mocks.mock_jsonrpc_empty_response import MOCK_JSONRPC_EMPTY_RESPONSE
from metamask_institutional.sdk.mocks.mock_jsonrpc_error_response import MOCK_JSONRPC_ERROR_RESPONSE
from metamask_institutional.sdk.mocks.mock_jsonrpc_get_tx_by_id import MOCK_JSONRPC_GET_TX_BY_ID
from metamask_institutional.sdk.mocks.mock_response import MockResponse


def mock_jsonrpc_requests_post(*args, **kwargs):
    """ This method will be used by the mock to replace requests.post"""

    json = kwargs["json"] if 'json' in kwargs else None
    method_field = json["method"] if json is not None and 'method' in json else None
    params_field = json["params"] if json is not None and 'params' in json else None
    from_field = params_field[0]["from"] if params_field is not None and len(params_field) > 0 and "from" in params_field[0] else None

    # Mock the request that creates the access token
    if args[0].__contains__('http://some-json-rpc-refresh-token-url'):
        return MockResponse({
            "access_token": "some-json-rpc-access-token",
            "refresh_token": "some-json-rpc-refresh-token",
            "token_type": "Bearer",
            "expires_in": 86400,
            "scope": ""
        }, 200)

    # Mock a response where no tx with passed id exists
    if params_field is not None and params_field.__contains__('bad-id'):
        return MockResponse(MOCK_JSONRPC_EMPTY_RESPONSE, 200)

    # Mock a response containing an error (this address is WETH's contract address, it's expected to fail)
    if from_field is not None and from_field.__contains__('0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2'):  # Bad address
        return MockResponse(MOCK_JSONRPC_ERROR_RESPONSE, 200)

    # Mock the request that gets a transaction by id
    if method_field is not None and method_field.__contains__('custodian_getTransactionById'):
        return MockResponse(MOCK_JSONRPC_GET_TX_BY_ID, 200)

    # Mock the request that creates a transaction by id
    if method_field is not None and method_field.__contains__('custodian_createTransaction'):
        return MockResponse(MOCK_JSONRPC_CREATE_TX_RESPONSE, 200)

    return MockResponse(None, 404)
