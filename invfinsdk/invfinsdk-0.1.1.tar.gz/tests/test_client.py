from unittest.mock import patch

from invfinsdk.client import Client


class TestClient:
    def test_base__base_build_url(self):
        assert (
            "https://inversionesyfinanzas.xyz/api/v1/" == Client("x")._base_build_url()
        )

    def test__build_request_params(self):
        path, params = Client("x")._build_request_params("path", {})
        assert "https://inversionesyfinanzas.xyz/api/v1/path/" == path
        assert {"api_key": "x"} == params

        path, params = Client("x")._build_request_params(
            "path2", {"param": 5, "param2": "second"}
        )
        assert "https://inversionesyfinanzas.xyz/api/v1/path2/" == path
        assert {
            "api_key": "x",
            "param": 5,
            "param2": "second",
        } == params

    @patch("requests.get")
    def test__perform_request(self, mock_request):
        Client("x")._perform_request("path", {})
        mock_request.assert_called_once_with(
            url="https://inversionesyfinanzas.xyz/api/v1/path/",
            params={"api_key": "x"},
            headers={"User-Agent": "invfinsdk-Python"},
        )
