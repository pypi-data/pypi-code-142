from src.usdplus import USDPlus

matic_network = USDPlus('m')

for line in matic_network.payouts():
    print(line)