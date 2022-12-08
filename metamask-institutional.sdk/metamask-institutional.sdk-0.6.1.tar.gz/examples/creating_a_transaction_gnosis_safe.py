import os

from metamask_institutional.sdk import CustodianFactory

# Instantiate the factory
factory = CustodianFactory()

# Grab your token from the environment, or anywhere else
token = os.environ["MMISDK_TOKEN_GNOSIS_SAFE_DEV"]

# Create the custodian, using the factory
custodian = factory.create_for("gnosis-safe-dev", token)

# Build tx details
tx_params = {
    "from": "0x1b6A48B065A449D70FC9aC0E77eec6a0aAf92F26",  # Address of the Gnosis Safe
    "to": "0xf979C4D970885322CF929902D778E0eA6Ac0f56f",
    "type": "2",
    "value": "1",  # in Wei
    "gas": "21000",
    "maxPriorityFeePerGas": "21000",
    "maxFeePerGas": "21000"
}
jsonrpc_extra_params = {
    "chainId": "0x4",
    "originUrl": "",  # Mandatory, but you can use an empty string
    "note": "This is a note to trader"
}

# Create the tx from details and send it to the custodian
transaction = custodian.create_transaction(tx_params, jsonrpc_extra_params)

print(type(transaction))
# <class 'metamask-institutional.sdk.common.transaction.Transaction'>

print(transaction)
# id='9fbbd8d1-ef8e-425a-8743-b1008ea22152'
# type='2'
# from_='0xb2c77973279baaaf48c295145802695631d50c01'
# to='0x57f36031E223FabC1DaF93B401eD9F4F1Acc6904'
# value='1'
# gas='21000'
# gasPrice=None
# maxPriorityFeePerGas='1500000014'
# maxFeePerGas='1500000000'
# nonce=None
# data='0xa9059cbb000000000000000000000000099dbbd63f749a9802526b277b8f3aaa3c5e81b0000000000000000000000000000000000000000000000000000000011ee39a80'
# hash=None
# status=TransactionStatus(finished=False, signed=False, submitted=False, success=False, displayText='Created', reason=None)
