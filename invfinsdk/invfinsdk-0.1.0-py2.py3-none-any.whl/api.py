from typing import Any, Dict, Union

from invfinsdk.client import Client
from invfinsdk.constants import (
    ALL_COMPANIES,
    ALL_EXCHANGES,
    ALL_INDUSTRIES,
    ALL_SECTORS,
    ALL_SUPERINVESTORS,
    ALL_TERMS,
    BALANCE_SHEET,
    CASHFLOW_STATEMENT,
    INCOME_STATEMENT,
    SINGLE_COMPANY_BASIC,
    SINGLE_COMPANY_FULL,
    SINGLE_SUPERINVESTOR_HISTORIAL,
    SINGLE_SUPERINVESTOR_MOVEMENTS,
    SINGLE_TERM,
)


class Exchange(Client):
    def get_all_exchanges(self) -> Dict[str, Any]:
        return self._get_clean_response(ALL_EXCHANGES)


class Industry(Client):
    def get_all_industries(self) -> Dict[str, Any]:
        return self._get_clean_response(ALL_INDUSTRIES)


class Sector(Client):
    def get_all_sectors(self) -> Dict[str, Any]:
        return self._get_clean_response(ALL_SECTORS)


class Company(Client):
    def get_all_companies(self) -> Dict[str, Any]:
        return self._get_clean_response(ALL_COMPANIES)

    def get_company_basic_information(
        self,
        params: Dict[str, Union[str, int]],
    ) -> Dict[str, Any]:
        return self._get_clean_response(SINGLE_COMPANY_BASIC, params)

    def get_company_full_information(
        self,
        params: Dict[str, Union[str, int]],
    ) -> Dict[str, Any]:
        return self._get_clean_response(SINGLE_COMPANY_FULL, params)

    def get_company(
        self,
        amount_info: str,
        params: Dict[str, Union[str, int]],
    ) -> Dict[str, Any]:
        """Get a single company using either his id or his ticker

        Parameters
        ----------
            params : Dict[str, Union[str, int]]
                Parameters to perform a lookup
                Example: {"ticker": "INTC"}

            amount_info : str
                Either full or basic

        Returns
        -------
            Dict[str, Any]
                A company full information
        """
        if amount_info == "basic":
            return self.get_company_basic_information(params)
        elif amount_info == "full":
            return self.get_company_full_information(params)
        raise Exception("You must set either full or basic")

    def get_company_income_statements(
        self,
        params: Dict[str, Union[str, int]],
    ) -> Dict[str, Any]:
        return self._get_clean_response(INCOME_STATEMENT, params)

    def get_company_balance_sheets(
        self,
        params: Dict[str, Union[str, int]],
    ) -> Dict[str, Any]:
        return self._get_clean_response(BALANCE_SHEET, params)

    def get_company_cashflow_statements(
        self,
        params: Dict[str, Union[str, int]],
    ) -> Dict[str, Any]:
        return self._get_clean_response(CASHFLOW_STATEMENT, params)


class Term(Client):
    def get_all_terms(self) -> Dict[str, Any]:
        return self._get_clean_response(ALL_TERMS)

    def get_term(self, params: Dict[str, Union[str, int]]) -> Dict[str, Any]:
        """Get a single term using either his id or his slug

        Parameters
        ----------
            params : Dict[str, Union[str, int]]
                Parameters to perform a lookup
                Example: {"slug": "precio-valor-en-libros"}

        Returns
        -------
            Dict[str, Any]
                A full term
        """
        return self._get_clean_response(SINGLE_TERM, params)


class SuperInvestor(Client):
    def get_all_superinvestors(self) -> Dict[str, Any]:
        return self._get_clean_response(ALL_SUPERINVESTORS)

    def get_superinvestor_historial(
        self,
        params: Dict[str, Union[str, int]],
    ) -> Dict[str, Any]:
        """Get all the historial of a superinvestor

        Parameters
        ----------
            params : Dict[str, Union[str, int]]
                Parameters to perform a lookup
                Example: {"id": 45}

        Returns
        -------
            Dict[str, Any]
                All the superinvestor historial
        """
        return self._get_clean_response(SINGLE_SUPERINVESTOR_HISTORIAL, params)

    def get_superinvestor_movements(
        self,
        params: Dict[str, Union[str, int]],
    ) -> Dict[str, Any]:
        """Get all the movements of a superinvestor

        Parameters
        ----------
            params : Dict[str, Union[str, int]]
                Parameters to perform a lookup
                Example: {"slug": "precio-valor-en-libros"}

        Returns
        -------
            Dict[str, Any]
                All the superinvestor movements
        """
        return self._get_clean_response(SINGLE_SUPERINVESTOR_MOVEMENTS, params)
