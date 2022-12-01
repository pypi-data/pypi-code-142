import decimal
import json
import os
import statistics
import time

from dotenv import load_dotenv
from eth_abi.packed import encode_abi_packed
from eth_account.messages import encode_defunct
from eth_utils import keccak
from web3.auto import w3

from starkware_helpers.signature import get_price_msg, sign

load_dotenv()


def starkex_sign(oracle_name_int, external_asset_padded, timestamp, external_price, private_key):
    """
    Starkex signs the given asset and price

    :param oralce_name_int: name of oracle converted from hex to int
    :param external_asset_padded: external asset being signed
    :param timestamp: timestamp of function invocation
    :param external_price: external price of given asset
    :param private_key: private key used for signing
    """
    data = get_price_msg(oracle_name_int, external_asset_padded, timestamp, external_price)
    r, s = sign(data, int(private_key, 16))
    signed = {"signature": {"r": hex(r), "s": hex(s)}, "timestamp": str(timestamp), "msg_hash": str(hex(data))}
    return signed


def evm_pack(evm_address, asset_pair: str, timestamp: int, price: int):
    """
    Equivalent to StarkEx's get_price_msg without hashing

    :param evm_address: evm address used to creating the given hash
    :param asset_pair: asset pair for the given price
    :param timestamp: timestamp of function invocation
    :param price: price of given asset-pair
    :return encode_defunct(hash): returns encoded hash for signing
    """
    concat_hash = keccak(encode_abi_packed(["address", "string", "uint256", "uint256"], [evm_address, asset_pair, timestamp, price]))
    return encode_defunct(concat_hash)


def evm_sign(evm_address, asset, timestamp, external_price, evm_private_key):
    """
    EVM signs the given asset and price

    :param evm_address: evm address for packing/signing
    :param asset: name of asset for the given external_price
    :param timestamp: timestamp of when the signing function is invoked
    :param external_price: price of given asset
    :param evm_private_key: evm private key used for signing message
    :return signed: returns struct with signature, timestamp, and hash
    """
    evm_packed_hash = evm_pack(evm_address, asset, timestamp, external_price)
    signed_evm_message = w3.eth.account.sign_message(evm_packed_hash, private_key=evm_private_key)
    signature = {"r": hex(signed_evm_message.r), "s": hex(signed_evm_message.s), "v": hex(signed_evm_message.v)}
    signed = {"signature": signature, "timestamp": str(timestamp), "msg_hash": "0x" + evm_packed_hash.body.hex()}
    return signed


def sign_prices(asset, external_price, oracle_name_hex, private_key, evm_address, evm_private_key):
    """
    Signs the given asset price using the provider's private key

    :param asset: name of asset (e.g. BTCUSD)
    :param external_price: asset price to sign
    :param oracle_name_hex: hex of oracle name string
    :param private_key: private key used to generate stark signed price
    :param evm_address: evm address used for signing
    :param evm_private_key: private key used to generate evm signed price
    :return starkex_signed_price, evm_signed_price: returns objects containing signed price dicts
    """
    oracle_name_int = int(oracle_name_hex, 16)
    timestamp = int(time.time())
    asset_hex = asset.encode("utf-8").hex()
    external_asset_padded_hex = "0x" + asset_hex + (32 - len(asset_hex)) * "0"

    stark_signed_price = {
        "external_asset_id": external_asset_padded_hex + oracle_name_hex,
        "price": str(external_price),
    }
    evm_signed_price = stark_signed_price.copy()

    external_asset_padded = int(external_asset_padded_hex, 16)
    stark_signed_price["timestamped_signature"] = starkex_sign(
        oracle_name_int, external_asset_padded, timestamp, external_price, private_key
    )
    evm_signed_price["external_asset_id"] = asset
    evm_signed_price["timestamped_signature"] = evm_sign(evm_address, asset, timestamp, external_price, evm_private_key)

    return stark_signed_price, evm_signed_price


async def send(oracle_name, asset, starkex_signed_price, evm_signed_price, stork_endpoint):
    """
    This function takes the give oracle and price data, and forwards it to the stork websocket

    :param oracle_name: name of sending oracle
    :param asset: name of asset (e.g. BTCUSD)
    :param starkex_signed_price: price value signed using starkex
    :param evm_signed_prices: price value signed using evm
    :param stork_endpoint: stork websocket connection
    """
    message = {
        "action": "price_update",
        "oracle_name": oracle_name,
        "asset": asset,
        "signed_price": starkex_signed_price,
        "evm_signed_price": evm_signed_price,
    }
    print(f"Sending message for asset {asset} to stork.")

    await stork_endpoint.send(json.dumps(message))


def median_price_update(close, prices, total, current_exchange, current_asset):
    """
    This function updates the given price dict and returns the median price for the given asset.

    :param close: close price of the given asset
    :param prices: dict containing prices of various assets
    :param total: array that stores current exchange prices for the given asset
    :param current_exchange: current exchange (e.g. cbse)
    :param current_asset: current asset (e.g. BTCUSD)
    :returns external_price: returns the calculated external price if data is valid

    Structure for the `prices` object is as follows:
    prices[]: Array containing asset names
    asset: Dict containing exchange namesb/values mapped to price objects
    current_exchange: set containing price and timestamp of price update

    Overall: prices[current_asset:{current_exchange:{"price":price, "timstamp":time}}]
    """
    if current_asset in prices:
        prices[current_asset].update(
            {
                current_exchange: {
                    "price": close,
                    "timestamp": int(time.time()),
                }
            }
        )
    else:
        # Add new entry if exchange data does not exist
        prices.update(
            {
                current_asset: {
                    current_exchange: {
                        "price": close,
                        "timestamp": int(time.time()),
                    }
                }
            }
        )

    # Remove data older than 10 seconds
    for exch in list(prices[current_asset]):
        timestamp = prices[current_asset][exch]["timestamp"]
        exch_price = prices[current_asset][exch]["price"]
        if (int(time.time()) - timestamp) < 10:
            total.append(exch_price)
        else:
            del prices[current_asset][exch]

    # Calculate and return the median price
    if len(total) > 0:
        median_price = statistics.median(total)
        return median_price


def quantize_price(median_price, exponent=18):
    """
    This function takes a given median price, and quantizes it to avoid float imprecisions.

    :param median_price: given median asset price
    :param exponent: optional param defines the exponent when multiplying(default = 18)
    :returns external_price: returns price after quantizing and multiplying by exponent
    """
    decimal_price = decimal.Decimal(median_price)
    quantized_price = decimal_price.quantize(decimal.Decimal(str(median_price)))
    external_price = int(quantized_price * (10**exponent))

    return external_price


def parse_env_vars(var_name):
    """
    This function takes a given environment variable name, and parses it from the .env file

    :param var_name_hex: given key of environment variable, which corresponds to a hex value stored in the .env file
    :returns parsed_var: returns env var converted into hexadecimal
    """
    parsed_var = hex(int(os.getenv(var_name), 16))

    return parsed_var


def can_skip_update(current_asset, median_price, last_updates):
    """
    This function checks the last_updates object to verify if a new update is needed to be sent or not.
    Uses a 10 basis points and 5 second check to decide whether or not to send a new update.

    :param current_asset: name of current asset being checked
    :param median_price: current median price of the given asset
    :param last_updates: stores the median and timestamp value of the last update for each asset sent by stork
    :returns bool: returns true if update should be ignored, and false if the update should be sent
    """
    last_median = last_updates[current_asset]["last_update"]["last_median"]
    last_time = last_updates[current_asset]["last_update"]["last_time"]
    if (int(time.time()) - last_time) < 5 and abs((median_price / last_median) - 1) < 0.001:
        return True

    return False
