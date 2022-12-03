from pledger.portfolio import Portfolio
from pledger.account import transfers, Account, Transfer
from pledger.interest import Interest, Interval


def main():
    transfer_1 = Transfer.deposit(100_000)

    acc = Account(
        transfers(transfer_1),
        interest=Interest(0.0425, True, Interval.DAILY),
        length_months=24,
    )

    # acc.calculate_final_balance()

    # print(acc.get_statement())
    # print(acc.get_balance())
    # print(acc.get_interest_balance())

    portfolio = Portfolio(105_000)

    portfolio.open_account(acc)

    portfolio.simulate(4)

    print(acc.get_interest_balance())


if __name__ == "__main__":
    main()
