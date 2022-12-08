from pydantic import constr

EthereumAddress = constr(regex="^0x[0-9a-fA-F]{40}$")
