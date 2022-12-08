
import unittest
from unittest import mock

import requests

from metamask_institutional.sdk.jsonrpc.jsonrpc_client import JsonRpcClient
from metamask_institutional.sdk.jsonrpc.jsonrpc_create_transaction_metadata import JsonRpcCreateTransactionMetadata
from metamask_institutional.sdk.jsonrpc.jsonrpc_create_transaction_params import JsonRpcCreateTransactionParams
from metamask_institutional.sdk.mocks.mock_jsonrpc_requests_post import mock_jsonrpc_requests_post


class JsonRpcClientTest(unittest.TestCase):
    """Test Class"""
    @classmethod
    def setUpClass(cls):
        cls.client = JsonRpcClient("http://some-json-rpc-url", "some-json-rpc-refresh-token", "http://some-json-rpc-refresh-token-url")

    def test_should_be_defined(self):
        self.assertIsNotNone(self.client)

    @mock.patch('requests.post', side_effect=mock_jsonrpc_requests_post)
    def test_should_create_access_token(self, mock_post):
        access_token, expires_in = self.client._JsonRpcClient__create_access_token()
        self.assertEqual(access_token, "some-json-rpc-access-token")
        self.assertEqual(expires_in, 86400)

    @mock.patch('requests.post', side_effect=mock_jsonrpc_requests_post)
    def test_should_get_headers(self, mock_post):
        headers = self.client._JsonRpcClient__get_headers()
        self.assertEqual(headers, {
            "Authorization": 'Bearer some-json-rpc-access-token'
        })

    @mock.patch('requests.post', side_effect=mock_jsonrpc_requests_post)
    def test_should_get_transaction_by_id(self, mock_post):
        get_transaction_result = self.client.get_transaction_by_id("ef8cb7af-1a00-4687-9f82-1f1c82fbef54")

        self.assertIsNotNone(get_transaction_result)
        self.assertEqual(get_transaction_result.id, "b903b4d6-bc70-435a-a289-24b04af0d78f")
        self.assertEqual(get_transaction_result.type, "0x2")
        self.assertEqual(get_transaction_result.from_, "0x367dacaf26cc1381f31911676ba40088938aa677")
        self.assertEqual(get_transaction_result.to, "0x7603A62b21A85f5cD02baE3389F35F1AcBaB0Ab2")
        self.assertEqual(get_transaction_result.value, "0x0")
        self.assertEqual(get_transaction_result.gas, "0x84c1")
        self.assertEqual(get_transaction_result.gasPrice, None)
        self.assertEqual(get_transaction_result.maxPriorityFeePerGas, "0x59682f00")
        self.assertEqual(get_transaction_result.maxFeePerGas, "0x596a67af")
        self.assertEqual(get_transaction_result.nonce, "0xa4f")
        self.assertEqual(get_transaction_result.data,
                         "0x97c5ed1e000000000000000000000000367dacaf26cc1381f31911676ba40088938aa6770000000000000000000000000000000000000000000000000de0b6b3a7640000")
        self.assertEqual(get_transaction_result.hash, "0x4b5981d66479ab1c7253de0b9e040dc2c74e38a5a005f1f253c9eb67cda31241")
        self.assertEqual(get_transaction_result.status.finished, True)
        self.assertEqual(get_transaction_result.status.submitted, True)
        self.assertEqual(get_transaction_result.status.signed, True)
        self.assertEqual(get_transaction_result.status.success, True)
        self.assertEqual(get_transaction_result.status.displayText, "Mined")
        self.assertEqual(get_transaction_result.status.reason, None)

    @mock.patch('requests.post', side_effect=mock_jsonrpc_requests_post)
    def test_get_transaction_by_id_with_bad_id_should_raise(self, mock_post):
        with self.assertRaises(requests.HTTPError):
            self.client.get_transaction_by_id("bad-id")

    @mock.patch('requests.post', side_effect=mock_jsonrpc_requests_post)
    def test_should_create_transaction(self, mock_post):
        jsonrpc_create_tx_params = JsonRpcCreateTransactionParams(
            type="0x2",
            from_="0x367dacaf26cc1381f31911676ba40088938aa677",
            to="0x57f36031E223FabC1DaF93B401eD9F4F1Acc6904",
            gas="0x5208",
            value="0x1",
            maxPriorityFeePerGas="0x59682f0e",
            maxFeePerGas="0x59682f0e"
        )
        jsonrpc_create_tx_metadata = JsonRpcCreateTransactionMetadata(
            chainId="0x4",
            originUrl="https://www.example.com",
            note="This is a note to trader"
        )
        tx_id = self.client.create_transaction(jsonrpc_create_tx_params, jsonrpc_create_tx_metadata)
        self.assertEqual(tx_id, "b903b4d6-bc70-435a-a289-24b04af0d78f")

    @mock.patch('requests.post', side_effect=mock_jsonrpc_requests_post)
    def test_create_transaction_with_bad_from_should_raise(self, mock_post):
        with self.assertRaises(requests.HTTPError):
            jsonrpc_create_tx_params = JsonRpcCreateTransactionParams(
                type="0x2",
                from_="0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2",  # Bad address
                to="0x57f36031E223FabC1DaF93B401eD9F4F1Acc6904",
                gas="0x5208",
                value="0x1",
                maxPriorityFeePerGas="0x59682f0e",
                maxFeePerGas="0x59682f0e"
            )
            jsonrpc_create_tx_metadata = JsonRpcCreateTransactionMetadata(
                chainId="0x4",
                originUrl="https://www.example.com",
                note="This is a note to trader"
            )
            self.client.create_transaction(jsonrpc_create_tx_params, jsonrpc_create_tx_metadata)

    @mock.patch('requests.post', side_effect=mock_jsonrpc_requests_post)
    def test___create_access_token_cached_should_call_once(self, mock_post):
        access_token_1 = self.client._JsonRpcClient__create_access_token_cached()
        access_token_2 = self.client._JsonRpcClient__create_access_token_cached()
        access_token_3 = self.client._JsonRpcClient__create_access_token_cached()
        access_token_4 = self.client._JsonRpcClient__create_access_token_cached()
        access_token_5 = self.client._JsonRpcClient__create_access_token_cached()
        mock_post.assert_called_once()
        self.assertEqual(access_token_1, access_token_2)
        self.assertEqual(access_token_2, access_token_3)
        self.assertEqual(access_token_3, access_token_4)
        self.assertEqual(access_token_4, access_token_5)


if __name__ == "__main__":
    unittest.main()
