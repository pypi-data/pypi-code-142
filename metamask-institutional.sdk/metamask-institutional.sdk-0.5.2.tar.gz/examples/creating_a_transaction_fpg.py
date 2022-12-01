import os

from metamask_institutional.sdk import CustodianFactory

# Instantiate the factory
factory = CustodianFactory()

# Grab your token from the environment, or anywhere else
token = os.environ["MMISDK_TOKEN_FPG_ALPHA"]

# Create the custodian, using the factory
custodian = factory.create_for("fpg-alpha", token)

# Build tx details
tx_params = {
    "from": "0x9BEe39bF784DDbEB0ae32BB1A7E7F927906C1da0",
    "to": "0x9BEe39bF784DDbEB0ae32BB1A7E7F927906C1da0",
    "type": "2",
    "value": "1",  # in Wei
    "gas": "21000",
    "maxPriorityFeePerGas": "21000",
    "maxFeePerGas": "21000"
}
jsonrpc_extra_params = {
    "chainId": "0x1",  # FPG supports mainnet only
    "note": "This is a note to trader"
}

# Create the tx from details and send it to the custodian
transaction = custodian.create_transaction(tx_params, jsonrpc_extra_params)

print(type(transaction))
# <class 'metamask-institutional.sdk.common.transaction.Transaction'>

print(transaction)
# id='2f0e06c0-b6d6-4c6b-b86f-518b1ed9f16d'
# type='2'
# from_='0x9BEe39bF784DDbEB0ae32BB1A7E7F927906C1da0'
# to='0x9BEe39bF784DDbEB0ae32BB1A7E7F927906C1da0'
# value='1'
# gas='21000'
# gasPrice=None
# maxPriorityFeePerGas='21000'
# maxFeePerGas='21000'
# nonce=None
# data=None
# hash=None
# status=TransactionStatus(finished=False, signed=False, submitted=True, success=False, displayText='FPG Transaction', reason='')
