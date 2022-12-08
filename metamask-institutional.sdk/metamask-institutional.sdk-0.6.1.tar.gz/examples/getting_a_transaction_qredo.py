import os

from metamask_institutional.sdk.factory.custodian_factory import CustodianFactory

# Instantiate the factory
factory = CustodianFactory()

# Grab your token from the environment, or anywhere else
token = os.environ["MMISDK_TOKEN_QREDO_DEV"]

custodian = factory.create_for("qredo-dev", token)

# Get the transaction
transaction = custodian.get_transaction("2ELvFICFt3RnXWdyxjkMvFN80xr")

print(type(transaction))
# <class 'metamask-institutional.sdk.common.transaction.Transaction'>

print(transaction)
# id='2ELvFICFt3RnXWdyxjkMvFN80xr'
# type='1'
# from_='0x62468FD916bF27A3b76d3de2e5280e53078e13E1'
# to='0x62468FD916bF27A3b76d3de2e5280e53078e13E1'
# value='1'
# gas='21000'
# gasPrice='1000'
# maxPriorityFeePerGas=None
# maxFeePerGas=None
# nonce='0'
# data=''
# hash=''
# status=TransactionStatus(finished=False, submitted=False, signed=False, success=False, displayText='Unknown', reason='Unknown')
