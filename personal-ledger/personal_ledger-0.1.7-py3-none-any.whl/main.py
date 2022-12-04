from pledger.account import transfers, Account, Transfer
from pledger.interest import Interest, Interval
from pprint import pprint


def main():
    transfer_1 = Transfer.deposit(1_000_00)

    acc = Account(
        transfers(transfer_1),
        interest=Interest(0.0425, False, Interval.MONTHLY),
        length_months=24,
    )

    for day in range(720):
        acc.calculate_daily_balance()

    pprint(acc.get_statement())
    pprint(acc.get_balance())
    # pprint(acc.transfers)


if __name__ == "__main__":
    main()
