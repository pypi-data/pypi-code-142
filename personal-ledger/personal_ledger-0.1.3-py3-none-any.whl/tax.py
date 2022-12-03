from enum import Enum


class TaxBand(Enum):
    STARTING = "starting"
    BASIC = "basic"
    HIGHER = "higher"
    ADDITIONAL = "additional"


class Tax:

    income_tax_rates = {
        TaxBand.STARTING: 0.1,
        TaxBand.BASIC: 0.2,
        TaxBand.HIGHER: 0.4,
        TaxBand.ADDITIONAL: 0.45,
    }

    personal_savings_allowance = {
        TaxBand.BASIC: 1_000,
        TaxBand.HIGHER: 500,
        TaxBand.ADDITIONAL: 0,
    }

    dividends_tax_rates = {
        TaxBand.BASIC: 0.0875,
        TaxBand.HIGHER: 0.3375,
        TaxBand.ADDITIONAL: 0.3935,
    }

    personal_allowance = 12_570

    personal_allowance_limit = 100_000

    dividend_allowance = 2_000

    def get_tax_band(self, income: float) -> TaxBand:
        taxable_income = self.get_taxable_income(income)

        if taxable_income <= 5_000:
            return TaxBand.STARTING
        elif taxable_income <= 37_700:
            return TaxBand.BASIC
        elif taxable_income <= 150_000:
            return TaxBand.HIGHER
        elif taxable_income > 150_000:
            return TaxBand.ADDITIONAL

    def get_income_tax_rate(self, income: float) -> float:
        return self.income_tax_rates[self.get_tax_band(income)]

    def get_dividends_tax_rate(self, income: float) -> float:
        return self.dividends_tax_rates[self.get_tax_band(income)]

    def get_taxable_income(self, income: float) -> float:
        pa = self.get_personal_allowance(income)
        taxable_income = income - pa

        return taxable_income if taxable_income > 0 else 0

    def get_personal_allowance(self, income: float) -> float:
        if income < self.personal_allowance_limit:
            return self.personal_allowance

        personal_allowance = (
            self.personal_allowance - (income - self.personal_allowance_limit) / 2
        )
        return personal_allowance if personal_allowance > 0 else 0

    def get_personal_savings_allowance(self, income: float) -> float:
        return self.personal_savings_allowance[self.get_tax_band(income)]

    def take_home_interest(self, income: float, interest: float) -> float:
        psa = self.get_personal_savings_allowance(income)
        if interest < psa:
            return interest

        return interest - (interest - psa) * self.get_income_tax_rate(income)

    def take_home_dividends(self, income: float, dividends: float) -> float:
        if dividends < self.dividend_allowance:
            return dividends

        return dividends - (
            dividends - self.dividend_allowance
        ) * self.get_dividends_tax_rate(income)


if __name__ == "__main__":
    from pprint import pprint

    t = Tax()
    income = 105_000

    pprint(t.take_home_interest(income, 2_500))
    pprint(t.take_home_dividends(income, 5000))
