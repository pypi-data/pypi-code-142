from unittest.mock import patch

import pytest

from invfinsdk.api import Company, Exchange, Industry, Sector, SuperInvestor, Term


class TestExchange:
    @patch("requests.get")
    def test_get_all_exchanges(self, mock_request):
        Exchange("key").get_all_exchanges()
        mock_request.assert_called_once_with(
            url="https://inversionesyfinanzas.xyz/api/v1/lista-exchanges/",
            params={"api_key": "key"},
            headers={"User-Agent": "invfinsdk-Python"},
        )


class TestIndustry:
    @patch("requests.get")
    def test_get_all_industries(self, mock_request):
        Industry("key").get_all_industries()
        mock_request.assert_called_once_with(
            url="https://inversionesyfinanzas.xyz/api/v1/lista-industrias/",
            params={"api_key": "key"},
            headers={"User-Agent": "invfinsdk-Python"},
        )


class TestSector:
    @patch("requests.get")
    def test_get_all_sectors(self, mock_request):
        Sector("key").get_all_sectors()
        mock_request.assert_called_once_with(
            url="https://inversionesyfinanzas.xyz/api/v1/lista-sectores/",
            params={"api_key": "key"},
            headers={"User-Agent": "invfinsdk-Python"},
        )


class TestCompany:
    @patch("requests.get")
    def test_get_all_companies(self, mock_request):
        Company("key").get_all_companies()
        mock_request.assert_called_once_with(
            url="https://inversionesyfinanzas.xyz/api/v1/lista-empresas/",
            params={"api_key": "key"},
            headers={"User-Agent": "invfinsdk-Python"},
        )

    @patch("requests.get")
    def test_get_company_basic_information(self, mock_request):
        Company("key").get_company_basic_information({"slug": "AAPL"})
        mock_request.assert_called_once_with(
            url="https://inversionesyfinanzas.xyz/api/v1/empresa-basica/",
            params={"slug": "AAPL", "api_key": "key"},
            headers={"User-Agent": "invfinsdk-Python"},
        )

    @patch("requests.get")
    def test_get_company_full_information(self, mock_request):
        Company("key").get_company_full_information({"slug": "AAPL"})
        mock_request.assert_called_once_with(
            url="https://inversionesyfinanzas.xyz/api/v1/empresa-completa/",
            params={"slug": "AAPL", "api_key": "key"},
            headers={"User-Agent": "invfinsdk-Python"},
        )

    @patch("invfinsdk.api.Company.get_company_basic_information")
    @patch("invfinsdk.api.Company.get_company_full_information")
    def test_get_company(
        self,
        mock_get_company_full_information,
        mock_get_company_basic_information,
    ):
        Company("key").get_company("basic", {"param": "params"})
        mock_get_company_basic_information.assert_called_once_with({"param": "params"})
        Company("key").get_company("full", {"param2": "params2"})
        mock_get_company_full_information.assert_called_once_with({"param2": "params2"})
        with pytest.raises(Exception):
            Company("key").get_company("wrong", {"param3": "params3"})

    @patch("requests.get")
    def test_get_company_income_statements(self, mock_request):
        Company("key").get_company_income_statements({"slug": "AAPL"})
        mock_request.assert_called_once_with(
            url="https://inversionesyfinanzas.xyz/api/v1/estado-resultados/",
            params={"slug": "AAPL", "api_key": "key"},
            headers={"User-Agent": "invfinsdk-Python"},
        )

    @patch("requests.get")
    def test_get_company_balance_sheets(self, mock_request):
        Company("key").get_company_balance_sheets({"slug": "AAPL"})
        mock_request.assert_called_once_with(
            url="https://inversionesyfinanzas.xyz/api/v1/balance-general/",
            params={"slug": "AAPL", "api_key": "key"},
            headers={"User-Agent": "invfinsdk-Python"},
        )

    @patch("requests.get")
    def test_get_company_cashflow_statements(self, mock_request):
        Company("key").get_company_cashflow_statements({"slug": "AAPL"})
        mock_request.assert_called_once_with(
            url="https://inversionesyfinanzas.xyz/api/v1/estado-flujo-efectivo/",
            params={"slug": "AAPL", "api_key": "key"},
            headers={"User-Agent": "invfinsdk-Python"},
        )


class TestTerm:
    @patch("requests.get")
    def test_get_all_terms(self, mock_request):
        Term("key").get_all_terms()
        mock_request.assert_called_once_with(
            url="https://inversionesyfinanzas.xyz/api/v1/lista-terminos/",
            params={"api_key": "key"},
            headers={"User-Agent": "invfinsdk-Python"},
        )

    @patch("requests.get")
    def test_get_term(self, mock_request):
        Term("key").get_term({"id": 1})
        mock_request.assert_called_once_with(
            url="https://inversionesyfinanzas.xyz/api/v1/termino/",
            params={"id": 1, "api_key": "key"},
            headers={"User-Agent": "invfinsdk-Python"},
        )


class TestSuperInvestor:
    @patch("requests.get")
    def test_get_all_superinvestors(self, mock_request):
        SuperInvestor("key").get_all_superinvestors()
        mock_request.assert_called_once_with(
            url="https://inversionesyfinanzas.xyz/api/v1/lista-superinversores/",
            params={"api_key": "key"},
            headers={"User-Agent": "invfinsdk-Python"},
        )

    @patch("requests.get")
    def test_get_superinvestor_historial(self, mock_request):
        SuperInvestor("key").get_superinvestor_historial({"id": 1})
        mock_request.assert_called_once_with(
            url="https://inversionesyfinanzas.xyz/api/v1/lista-historial/",
            params={"id": 1, "api_key": "key"},
            headers={"User-Agent": "invfinsdk-Python"},
        )

    @patch("requests.get")
    def test_get_superinvestor_movements(self, mock_request):
        SuperInvestor("key").get_superinvestor_movements({"id": 1})
        mock_request.assert_called_once_with(
            url="https://inversionesyfinanzas.xyz/api/v1/lista-movimientos/",
            params={"id": 1, "api_key": "key"},
            headers={"User-Agent": "invfinsdk-Python"},
        )
