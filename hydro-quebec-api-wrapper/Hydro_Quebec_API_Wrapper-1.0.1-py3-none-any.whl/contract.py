"""Hydroquebec contract module."""
import logging
from collections.abc import Callable, Iterator
from datetime import date, datetime, timedelta
from io import StringIO

from hydroqc.hydro_api.client import HydroClient
from hydroqc.logger import get_logger
from hydroqc.winter_credit.consts import EST_TIMEZONE
from hydroqc.winter_credit.handler import WinterCreditHandler

from hydroqc.types import (
    ConsoAnnualTyping,
    ConsoDailyTyping,
    ConsoHourlyTyping,
    ConsoMonthlyTyping,
    PeriodDataTyping,
    listeContratModelTyping,
)


def check_period_data_present(
    method: Callable[..., None | str | bool | float]
) -> Callable[..., None | str | bool | float]:
    """Check if contract's data are present."""

    def wrapper(contract: "Contract") -> None | str | bool | float:
        if len(contract._all_period_data):
            return method(contract)

        contract._logger.warning("You need to call get_latest_period_info method first")
        return None

    return wrapper


def check_info_data_present(
    method: Callable[..., None | str | bool | float | date]
) -> Callable[..., None | str | bool | float | date]:
    """Check if contract's data are present."""

    def wrapper(contract: "Contract") -> None | str | bool | float | date:
        if hasattr(contract, "_raw_info_data"):
            return method(contract)

        contract._logger.warning("You need to call get_info method first")
        return None

    return wrapper


class Contract:
    """Hydroquebec contract.

    Represents a contract (contrat)
    """

    _mve_activated: bool
    _rate_code: str
    _rate_option_code: str | None
    _meter_id: str
    _address: str
    _raw_info_data: listeContratModelTyping

    def __init__(
        self,
        applicant_id: str,
        customer_id: str,
        account_id: str,
        contract_id: str,
        hydro_client: HydroClient,
        log_level: str | None = None,
    ):
        """Create a new Hydroquebec contract."""
        self._logger: logging.Logger = get_logger(
            f"c-{contract_id}",
            log_level=log_level,
            parent=f"w-{applicant_id}.c-{customer_id}.a-{account_id}",
        )
        self._no_partenaire_demandeur: str = applicant_id
        self._no_partenaire_titulaire: str = customer_id
        self._no_compte_contrat: str = account_id
        self._no_contrat: str = contract_id
        self._hydro_client: HydroClient = hydro_client
        wch_logger = self._logger.getChild("wch")
        self._wch: WinterCreditHandler = WinterCreditHandler(
            self.applicant_id,
            self.customer_id,
            self.contract_id,
            hydro_client,
            wch_logger,
        )
        self._address: str = ""
        self._all_period_data: list[PeriodDataTyping] = []
        self._rate_option_code = None

    @property
    def applicant_id(self) -> str:
        """Get applicant id."""
        return self._no_partenaire_demandeur

    @property
    def customer_id(self) -> str:
        """Get customer id."""
        return self._no_partenaire_titulaire

    @property
    def account_id(self) -> str:
        """Get account id."""
        return self._no_compte_contrat

    @property
    def contract_id(self) -> str:
        """Get contract id."""
        return self._no_contrat

    @property
    def winter_credit(self) -> WinterCreditHandler:
        """Get winter credit helper object."""
        return self._wch

    def set_preheat_duration(self, duration: int) -> None:
        """Set preheat duration in minutes."""
        self._wch.set_preheat_duration(duration)

    async def get_today_hourly_consumption(self) -> ConsoHourlyTyping:
        """Fetch hourly consumption for today."""
        return await self._hydro_client.get_today_hourly_consumption(
            self.applicant_id, self.customer_id, self.contract_id
        )

    async def get_hourly_consumption(self, date_wanted: str) -> ConsoHourlyTyping:
        """Fetch hourly consumption for a date."""
        return await self._hydro_client.get_hourly_consumption(
            self.applicant_id, self.customer_id, self.contract_id, date_wanted
        )

    async def get_daily_consumption(
        self, start_date: str, end_date: str
    ) -> ConsoDailyTyping:
        """Fetch daily consumption."""
        return await self._hydro_client.get_daily_consumption(
            self.applicant_id, self.customer_id, self.contract_id, start_date, end_date
        )

    async def get_today_daily_consumption(self) -> ConsoDailyTyping:
        """TODO ????.

        .. todo::
            document this method
        """
        today = datetime.today().astimezone(EST_TIMEZONE)
        yesterday = today - timedelta(days=1)
        start_date = yesterday.strftime("%Y-%m-%d")
        end_date = today.strftime("%Y-%m-%d")
        return await self.get_daily_consumption(start_date, end_date)

    async def get_monthly_consumption(self) -> ConsoMonthlyTyping:
        """Fetch monthly consumption."""
        return await self._hydro_client.get_monthly_consumption(
            self.applicant_id, self.customer_id, self.contract_id
        )

    async def get_annual_consumption(self) -> ConsoAnnualTyping:
        """Fetch annual consumption."""
        return await self._hydro_client.get_annual_consumption(
            self.applicant_id, self.customer_id, self.contract_id
        )

    async def get_info(self) -> listeContratModelTyping:
        """Fetch info about this contract."""
        self._logger.info("Get contract info")
        self._raw_info_data = await self._hydro_client.get_contract_info(
            self.applicant_id, self.customer_id, self.account_id, self.contract_id
        )
        self._wch.set_enabled(self._raw_info_data.get("optionTarifActuel") == "CPC")
        return self._raw_info_data

    async def get_periods_info(self) -> list[PeriodDataTyping]:
        """Fetch periods info."""
        self._all_period_data = await self._hydro_client.get_periods_info(
            self.applicant_id, self.customer_id, self.contract_id
        )
        return self._all_period_data

    def get_latest_period_info(self) -> PeriodDataTyping | dict[None, None]:
        """Fetch latest period info."""
        if self._all_period_data:
            return self._all_period_data[0]
        return {}

    async def get_daily_energy_and_power(
        self,
        start_date: str,
        end_date: str,
        raw_output: bool = False,
    ) -> Iterator[list[str | int | float]] | StringIO:
        """Get daily energy and power data on a specific date range.

        date format: 2022-11-23
        """
        data_csv = await self._hydro_client.get_conso_csv(
            self.applicant_id,
            self.customer_id,
            self.contract_id,
            start_date,
            end_date,
            "puissance-jour",
            raw_output,
        )
        return data_csv

    async def get_daily_energy(
        self,
        start_date: str,
        end_date: str,
        raw_output: bool = False,
    ) -> Iterator[list[str | int | float]] | StringIO:
        """Get daily energy and power data on a specific date range.

        date format: 2022-11-23
        """
        data_csv = await self._hydro_client.get_conso_csv(
            self.applicant_id,
            self.customer_id,
            self.contract_id,
            start_date,
            end_date,
            "energie-jour",
            raw_output,
        )
        return data_csv

    async def get_hourly_energy(
        self,
        start_date: str,
        end_date: str,
        raw_output: bool = False,
    ) -> Iterator[list[str | int | float]] | StringIO:
        """Get hourly energy on a specific date range.

        date format: 2022-11-23
        """
        data_csv = await self._hydro_client.get_conso_csv(
            self.applicant_id,
            self.customer_id,
            self.contract_id,
            start_date,
            end_date,
            "energie-heure",
            raw_output,
        )
        return data_csv

    async def get_power_demanded_per_15min(
        self,
        start_date: str,
        end_date: str,
        raw_output: bool = False,
    ) -> Iterator[list[str | int | float]] | StringIO:
        """Get power demande per 15 min on a specific date range.

        date format: 2022-11-23
        """
        data_csv = await self._hydro_client.get_conso_csv(
            self.applicant_id,
            self.customer_id,
            self.contract_id,
            start_date,
            end_date,
            "puissance-min",
            raw_output,
        )
        return data_csv

    async def get_consumption_overview_csv(
        self,
        raw_output: bool = False,
    ) -> Iterator[list[str | int | float]] | StringIO:
        """Get the consumption overview over the last 2 years."""
        data_csv = await self._hydro_client.get_conso_overview_csv(
            self.applicant_id,
            self.customer_id,
            self.contract_id,
            raw_output,
        )
        return data_csv

    @property
    @check_info_data_present
    def start_date(self) -> date:
        """Get contract start date."""
        start_date = date.fromisoformat(
            self._raw_info_data["dateDebutContrat"].split("T")[0]
        )
        return start_date

    @property
    @check_info_data_present
    def rate(self) -> str:
        """Get current period rate name."""
        return self._raw_info_data["tarifActuel"]

    @property
    @check_info_data_present
    def rate_option(self) -> str | None:
        """Get current period rate option name."""
        return self._raw_info_data.get("optionTarifActuel")

    @property
    @check_info_data_present
    def address(self) -> str:
        """Get contract address."""
        return self._raw_info_data["adresseConsommation"].strip()

    @property
    @check_info_data_present
    def meter_id(self) -> str:
        """Get meter id."""
        return self._raw_info_data["noCompteur"]

    # Current period properties
    # CP == Current period
    @property
    @check_period_data_present
    def cp_current_day(self) -> int:
        """Get number of days since the current period started."""
        return self._all_period_data[0]["nbJourLecturePeriode"]

    @property
    @check_period_data_present
    def cp_duration(self) -> int:
        """Get current period duration in days."""
        return self._all_period_data[0]["nbJourPrevuPeriode"]

    @property
    @check_period_data_present
    def cp_current_bill(self) -> float:
        """Get current bill since the current period started."""
        return self._all_period_data[0]["montantFacturePeriode"]

    @property
    @check_period_data_present
    def cp_projected_bill(self) -> float:
        """Projected bill of the current period."""
        return self._all_period_data[0]["montantProjetePeriode"]

    @property
    @check_period_data_present
    def cp_daily_bill_mean(self) -> float:
        """Daily bill mean since the current period started."""
        return self._all_period_data[0]["moyenneDollarsJourPeriode"]

    @property
    @check_period_data_present
    def cp_daily_consumption_mean(self) -> float:
        """Daily consumption mean since the current period started."""
        return self._all_period_data[0]["moyenneKwhJourPeriode"]

    @property
    @check_period_data_present
    def cp_total_consumption(self) -> float:
        """Total consumption since the current period started."""
        return self._all_period_data[0]["consoTotalPeriode"]

    @property
    @check_period_data_present
    def cp_projected_total_consumption(self) -> float:
        """Projected consumption of the current period started."""
        return self._all_period_data[0]["consoTotalProjetePeriode"]

    @property
    @check_period_data_present
    def cp_lower_price_consumption(self) -> float:
        """Total lower priced consumption since the current period started."""
        return self._all_period_data[0]["consoRegPeriode"]

    @property
    @check_period_data_present
    def cp_higher_price_consumption(self) -> float:
        """Total higher priced consumption since the current period started."""
        return self._all_period_data[0]["consoHautPeriode"]

    @property
    @check_period_data_present
    def cp_average_temperature(self) -> float:
        """Average temperature since the current period started."""
        return self._all_period_data[0]["tempMoyennePeriode"]

    @property
    @check_period_data_present
    def cp_kwh_cost_mean(self) -> float | None:
        """Mean cost of a kWh since the current period started."""
        if self._all_period_data[0]["coutCentkWh"] is not None:
            return self._all_period_data[0]["coutCentkWh"] / 100
        return None

    @property
    @check_period_data_present
    def cp_epp_enabled(self) -> bool:
        """Is EPP enabled for the current period.

        See: https://www.hydroquebec.com/residential/customer-space/
             account-and-billing/equalized-payments-plan.html
        """
        return self._all_period_data[0]["indMVEPeriode"]

    def __repr__(self) -> str:
        """Represent object."""
        return (
            f"""<Contract - {self.applicant_id} - {self.customer_id} - """
            f"""{self.account_id} - {self.contract_id}>"""
        )
