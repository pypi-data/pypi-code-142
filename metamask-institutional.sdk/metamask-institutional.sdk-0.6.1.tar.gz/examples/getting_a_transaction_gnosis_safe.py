import os

from metamask_institutional.sdk.factory.custodian_factory import CustodianFactory

# Instantiate the factory
factory = CustodianFactory()

# Grab your token from the environment, or anywhere else
token = os.environ["MMISDK_TOKEN_GNOSIS_SAFE_DEV"]
custodian = factory.create_for("gnosis-safe-dev", token)

# Get the transaction
transaction = custodian.get_transaction("0x603fd460b1ba00c1eea0f082e1cdd7fe596c8f7d0f588eab7da1e6273402e522")

print(type(transaction))
# <class 'metamask-institutional.sdk.common.transaction.Transaction'>

print(transaction)
# id='5377c945-f756-4c25-902d-c0d3b9cd179b'
# type='2'
# from_='0x033e270c08c3f297f99660f958d5f615207c1adf'
# to='0x7603A62b21A85f5cD02baE3389F35F1AcBaB0Ab2'
# value='0'
# gas='33997'
# gasPrice=None
# maxPriorityFeePerGas='1500000000'
# maxFeePerGas='19245046202'
# nonce='91'
# data='0x97c5ed1e000000000000000000000000033e270c08c3f297f99660f958d5f615207c1adf0000000000000000000000000000000000000000000000000de0b6b3a7640000'
# hash='0xe8073973a8ba8ba8d28b8a60e705c89f2facca54262fbc88a4f26f373ac29c81'
# status=TransactionStatus(finished=True, signed=True, submitted=True, success=True, displayText='Mined', reason=None)
