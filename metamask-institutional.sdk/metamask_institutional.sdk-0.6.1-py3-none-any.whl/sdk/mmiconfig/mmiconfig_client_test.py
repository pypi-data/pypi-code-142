
import unittest
from unittest import mock

from metamask_institutional.sdk.mmiconfig.mmiconfig_client import MMIConfigClient
from metamask_institutional.sdk.mocks.mock_mmiconfig_requests_get import mock_mmiconfig_requests_get


class CustodianConfigClientTest(unittest.TestCase):
    """Test Class"""
    @classmethod
    def setUpClass(cls):
        cls.client = MMIConfigClient()

    def test_should_be_defined(self):
        self.assertIsNotNone(self.client)

    @mock.patch('requests.get', side_effect=mock_mmiconfig_requests_get)
    def test_should_get_mmi_config(self, mock_get):
        mmi_config = self.client._MMIConfigClient__get_mmi_config("mock-mmi-config-api-url")
        self.assertIsNotNone(mmi_config)
        self.assertEqual(len(mmi_config.custodians), 1)
        self.assertEqual(mmi_config.custodians[0].refreshTokenUrl, "https://hi.ho")

    @mock.patch('requests.get', side_effect=mock_mmiconfig_requests_get)
    def test_should_get_merged_custodian_configs(self, mock_get):
        """ There are  6 legacy """
        custodian_configs = self.client.get_merged_custodian_configs()
        self.assertIsNotNone(custodian_configs)
        self.assertEqual(len(custodian_configs), 8)  # 6 legacy custodian + 2 prod + 1 dev - 1 override (qredo)


if __name__ == "__main__":
    unittest.main()
