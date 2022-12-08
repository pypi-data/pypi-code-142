
import unittest
from unittest import mock

from metamask_institutional.sdk.adapters.jsonrpc_adapter import JsonRpcAdapter
from metamask_institutional.sdk.common.transaction import Transaction
from metamask_institutional.sdk.jsonrpc.jsonrpc_client import JsonRpcClient
from metamask_institutional.sdk.mocks.mock_jsonrpc_requests_post import mock_jsonrpc_requests_post
from metamask_institutional.sdk.mocks.mock_legacy_tx_params import MOCK_LEGACY_TX_PARAMS


class JsonRpcAdapterTest(unittest.TestCase):
    """Test Class"""
    @classmethod
    def setUpClass(cls):
        client = JsonRpcClient("http://some-url", "some-json-rpc-refresh-token", "http://some-json-rpc-refresh-token-url")
        cls.custodian = JsonRpcAdapter(client)

    def test_should_be_defined(self):
        self.assertIsNotNone(self.custodian)

    @mock.patch('requests.post', side_effect=mock_jsonrpc_requests_post)
    def test_should_get_transaction(self, mock_get):
        transaction = self.custodian.get_transaction("b903b4d6-bc70-435a-a289-24b04af0d78f")
        self.__verify(transaction)

    @mock.patch('requests.post', side_effect=mock_jsonrpc_requests_post)
    def test_should_create_transaction(self, mock_post):
        extra_params = {
            "chainId": "0x4",
            "originUrl": "https://www.example.com",
            "note": "This is a note to trader"
        }
        transaction = self.custodian.create_transaction(MOCK_LEGACY_TX_PARAMS, extra_params)
        self.assertEqual(transaction.id, 'b903b4d6-bc70-435a-a289-24b04af0d78f')
        self.__verify(transaction)

    def __verify(self, transaction: Transaction) -> None:
        self.assertEqual(transaction.id, 'b903b4d6-bc70-435a-a289-24b04af0d78f')
        self.assertEqual(transaction.type, "2")
        self.assertEqual(transaction.from_, "0x367dacaf26cc1381f31911676ba40088938aa677")
        self.assertEqual(transaction.to, "0x7603A62b21A85f5cD02baE3389F35F1AcBaB0Ab2")
        self.assertEqual(transaction.value, "0")
        self.assertEqual(transaction.gas, "33985")
        self.assertEqual(transaction.gasPrice, None)
        self.assertEqual(transaction.maxPriorityFeePerGas, "1500000000")
        self.assertEqual(transaction.maxFeePerGas, "1500145583")
        self.assertEqual(transaction.nonce, "2639")
        self.assertEqual(
            transaction.data, "0x97c5ed1e000000000000000000000000367dacaf26cc1381f31911676ba40088938aa6770000000000000000000000000000000000000000000000000de0b6b3a7640000")
        self.assertEqual(transaction.hash, "0x4b5981d66479ab1c7253de0b9e040dc2c74e38a5a005f1f253c9eb67cda31241")
        self.assertEqual(transaction.status.finished, True)
        self.assertEqual(transaction.status.submitted, True)
        self.assertEqual(transaction.status.signed, True)
        self.assertEqual(transaction.status.success, True)
        self.assertEqual(transaction.status.displayText, "Mined")
        self.assertEqual(transaction.status.reason, None)


if __name__ == "__main__":
    unittest.main()
