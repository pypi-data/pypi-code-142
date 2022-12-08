import os

from metamask_institutional.sdk.factory.custodian_factory import CustodianFactory

# Instantiate the factory
factory = CustodianFactory()

# Grab your token from the environment, or anywhere else
token = os.environ["MMISDK_TOKEN_FPG_ALPHA"]
custodian = factory.create_for("fpg-alpha", token)

# Get the transaction
transaction = custodian.get_transaction("2ab09f15-3a7d-47fe-a8df-ba88af80f941")

print(type(transaction))
# <class 'metamask-institutional.sdk.common.transaction.Transaction'>

print(transaction)
# id='2ab09f15-3a7d-47fe-a8df-ba88af80f941'
# type='2'
# from_='0x9BEe39bF784DDbEB0ae32BB1A7E7F927906C1da0'
# to='0x9BEe39bF784DDbEB0ae32BB1A7E7F927906C1da0'
# value='1'
# gas='21000'
# gasPrice=None
# maxPriorityFeePerGas='1500000014'
# maxFeePerGas='1500000014'
# nonce=None
# data=None
# hash=None
# status=TransactionStatus(finished=False, signed=False, submitted=True, success=False, displayText='FPG Transaction', reason='')
