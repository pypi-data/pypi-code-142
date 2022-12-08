import unittest
from unittest.mock import patch

from metamask_institutional.sdk.adapters.bitgo_adapter import BitgoAdapter
from metamask_institutional.sdk.adapters.cactus_adapter import CactusAdapter
from metamask_institutional.sdk.adapters.jsonrpc_adapter import JsonRpcAdapter
from metamask_institutional.sdk.adapters.qredo_adapter import QredoAdapter
from metamask_institutional.sdk.factory.custodian_factory import CustodianFactory
from metamask_institutional.sdk.mocks.mock_mmiconfig_requests_get import mock_mmiconfig_requests_get


class CustodianFactoryTest(unittest.TestCase):

    @patch('requests.get', side_effect=mock_mmiconfig_requests_get)
    def test_should_be_defined(self, mock_get):
        factory = CustodianFactory()
        self.assertIsNotNone(factory)

    @patch('requests.get', side_effect=mock_mmiconfig_requests_get)
    def test_should_fetch_configs(self, mock_requests):
        factory = CustodianFactory()
        self.assertIsNotNone(factory.custodians_config)
        self.assertGreater(len(factory.custodians_config), 0)

    @patch('requests.get', side_effect=mock_mmiconfig_requests_get)
    def test_should_get_supported_custodians(self, mock_requests):
        factory = CustodianFactory()
        supported_custodians = factory.get_supported_custodians()
        self.assertEqual(8, len(supported_custodians))
        self.assertIn("qredo", supported_custodians)
        self.assertIn("qredo-dev", supported_custodians)
        self.assertIn("cactus", supported_custodians)
        self.assertIn("cactus-dev", supported_custodians)
        self.assertIn("bitgo", supported_custodians)
        self.assertIn("bitgo-test", supported_custodians)
        self.assertIn("saturn", supported_custodians)

    @patch('requests.get', side_effect=mock_mmiconfig_requests_get)
    def test_should_create_custodian(self, mock_requests):
        factory = CustodianFactory()
        custodian = factory.create_for("qredo", "refresh_token")
        self.assertIsNotNone(custodian)
        self.assertIsInstance(custodian, QredoAdapter)
        custodian = factory.create_for("qredo-dev", "refresh_token")
        self.assertIsNotNone(custodian)
        self.assertIsInstance(custodian, QredoAdapter)
        custodian = factory.create_for("cactus", "refresh_token")
        self.assertIsNotNone(custodian)
        self.assertIsInstance(custodian, CactusAdapter)
        custodian = factory.create_for("cactus-dev", "refresh_token")
        self.assertIsNotNone(custodian)
        self.assertIsInstance(custodian, CactusAdapter)
        custodian = factory.create_for("bitgo", "refresh_token")
        self.assertIsNotNone(custodian)
        self.assertIsInstance(custodian, BitgoAdapter)
        custodian = factory.create_for("bitgo-test", "refresh_token")
        self.assertIsNotNone(custodian)
        self.assertIsInstance(custodian, BitgoAdapter)
        custodian = factory.create_for("saturn", "refresh_token")
        self.assertIsNotNone(custodian)
        self.assertIsInstance(custodian, JsonRpcAdapter)

    @patch('requests.get', side_effect=mock_mmiconfig_requests_get)
    def test_should_fail_unsupported_custodian(self, mock_requests):
        factory = CustodianFactory()
        with self.assertRaises(AssertionError):
            factory.create_for("whatever", "refresh_token")


if __name__ == "__main__":
    unittest.main()
