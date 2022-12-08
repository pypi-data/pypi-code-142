from datetime import date
from typing import Optional
from uuid import UUID

from serenity_types.utils.serialization import CamelModel
from serenity_types.valuation.core import CashTreatment, MarkTime


class PricingContext(CamelModel):
    """
    Standard settings to use when doing pricing for risk calculation purposes,
    portfolio valuation, etc.. Generally controls which prices to select and
    how to convert those prices into the organization's base currency.
    """

    as_of_date: Optional[date] = None
    """
    The date on which the portfolio was valued; default to latest date.
    """

    mark_time: Optional[MarkTime] = MarkTime.UTC
    """
    The close time convention to use for close-on-close prices in the 24x7 market.
    """

    base_currency_id: Optional[UUID] = None
    """
    The accounting currency to use for valuation, reporting, etc., e.g. fund reports in USD.
    """

    cash_treatment: Optional[CashTreatment] = CashTreatment.FIAT_ONLY
    """
    What to consider to be a cash position, e.g. for NAV calcs.
    """
