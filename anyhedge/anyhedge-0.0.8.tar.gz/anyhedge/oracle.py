# Built-in imports
from __future__ import annotations
from codecs import decode
from dataclasses import dataclass
from functools import cached_property
from typing import (
    Sequence,
    Type,
)

# Library imports
from arrow import Arrow

# Local imports
from . import validators
from .bch_primitives import (
    PublicKey,
    ScriptTimestamp,
)

# Oracle prices are stored and limited to a 4 byte field.
# It may be unsigned, but I'm not sure so I use 31 bits to be safe
ORACLE_MAX_PRICE = (2 ** 31) - 1
GENERIC_4_BYTE_NUMBER = 2 ** 30


@dataclass(frozen=False)
class StrictPricepoints:
    """Sorted, unique pricepoints all from the same oracle"""
    all: Sequence[Pricepoint, ...]

    def __post_init__(self):
        # first validate oracle pubkeys (definitely die if mixed oracles)
        if self.all:
            oracle_pubkey = self.all[0].oracle_pubkey
            for p in self.all:
                validators.equal(p.oracle_pubkey, oracle_pubkey)

        # enforce uniqueness by timestamp
        lookup = {}
        for p in self.all:
            existing = lookup.get(p.timestamp)
            if existing is None:
                lookup[p.timestamp] = p
            else:
                if p == existing:
                    pass  # it's just a duplicate
                else:
                    raise ValueError(f'same timestamp, same oracle, different value: {p} vs {existing}')

        # enforce sorting
        self.all = tuple(sorted(lookup.values(), key=lambda p: p.timestamp))

    def __str__(self):
        return f'StrictPricepoints: {len(self.all)} prices for {self.all[0].oracleUnit_name}'

    def __repr__(self):
        return self.__str__()


def interleave_pricepoints(pricepoints_by_oracle_pubkey: dict[PublicKey, StrictPricepoints]) -> list[Pricepoint]:
    # TODO: There could be duplicates or bad overlapping messages hiding in this
    #       To solve that, make a formalized PricepointsByOracle class that strongly validates match between pubkey and pricepoints
    # let the optimized sorting algorithm sort it out even though we could do it in O(n) manually
    all_pricepoints = sum((list(p.all) for p in pricepoints_by_oracle_pubkey.values()), start=[])
    all_pricepoints.sort(key=lambda p: p.timestamp)
    return all_pricepoints


@dataclass(frozen=True)
class Pricepoint:
    oracle_pubkey: PublicKey
    message: str
    signature: str | None

    def __post_init__(self):
        # cheat for some early validation
        _, _, _, _ = self._message_parts

    def __str__(self):
        return f'{self.price_oracleUnits_per_bch} {self.oracleUnit_name} @ {self.timestamp} ({Arrow.utcfromtimestamp(self.timestamp)})'

    def __repr__(self):
        return self.__str__()

    @property
    def oracleUnit_name(self) -> str:
        return oracle_pubkey_to_unit_class[self.oracle_pubkey].name_of_oracleUnits

    @property
    def standardUnit_name(self) -> str:
        return oracle_pubkey_to_unit_class[self.oracle_pubkey].name_of_standardUnits

    @property
    def timestamp(self) -> ScriptTimestamp:
        return self._message_parts[0]

    @property
    def message_sequence(self) -> int:
        return self._message_parts[1]

    @property
    def price_sequence(self) -> int:
        return self._message_parts[2]

    @property
    def price_oracleUnits_per_bch(self) -> ScriptPriceInOracleUnitsPerBch:
        return ScriptPriceInOracleUnitsPerBch(self._message_parts[3])

    @property
    def price_standardUnits_per_bch(self) -> float:
        return float(self.price_oracleUnits_per_bch) / oracle_pubkey_to_unit_class[self.oracle_pubkey].oracleUnits_per_standardUnit

    @cached_property
    def _message_parts(self):
        # timestamp, message_sequence, price_sequence, price
        return parse_oracle_price_message(self.message)

    @classmethod
    def new_from_details(cls,
                         oracle_pubkey: PublicKey,
                         timestamp: ScriptTimestamp,
                         price_oracleUnits_per_bch: ScriptPriceInOracleUnitsPerBch,
                         message_sequence: int  = GENERIC_4_BYTE_NUMBER,
                         price_sequence: int  = GENERIC_4_BYTE_NUMBER,
                         signature: str | None = None,
                         ) -> Pricepoint:
        message_parts = []
        for data in (timestamp, message_sequence, price_sequence, price_oracleUnits_per_bch):
            message_parts.append(_swap_hex_endianness(f'{data:08x}'))
        message = ''.join(message_parts)
        pricepoint = Pricepoint(oracle_pubkey=oracle_pubkey, message=message, signature=signature)

        # do a sanity reverse check on the parsed values
        validators.equal(pricepoint.timestamp, timestamp)
        validators.equal(pricepoint.price_oracleUnits_per_bch, price_oracleUnits_per_bch)
        validators.equal(pricepoint.message_sequence, message_sequence)
        validators.equal(pricepoint.price_sequence, price_sequence)

        return pricepoint


class OracleUnit(float):
    name_of_oracleUnits: str = None
    name_of_standardUnits: str = None
    oracleUnits_per_standardUnit: int = None
    public_key: PublicKey = None

    def __init__(self, value):
        super().__init__()
        validators.instance(value, float)  # i.e. don't allow silent coercion
        # validators.greater_equal(self, 0)

    def __eq__(self, other: OracleUnit):
        if self.name_of_oracleUnits != other.name_of_oracleUnits:
            return False
        if self.name_of_standardUnits != other.name_of_standardUnits:
            return False
        if self.oracleUnits_per_standardUnit != other.oracleUnits_per_standardUnit:
            return False
        if self.public_key != other.public_key:
            return False
        if float(self) != float(other):
            return False
        return True

    def __hash__(self):
        return self.public_key

    @property
    def in_standard_units(self) -> float:
        return float(self) / self.oracleUnits_per_standardUnit


class ScriptPriceInOracleUnitsPerBch(int):
    def __new__(cls, value, *args, **kwargs):
        return super().__new__(cls, value)

    def __init__(self, value):
        super().__init__()
        validators.instance(value, int)  # i.e. don't allow silent coercion
        validators.less_equal(self, ORACLE_MAX_PRICE)
        validators.greater_equal(self, 1)


class BtcEM6Beta(OracleUnit):
    name_of_oracleUnits = 'BTC(e-6)'
    name_of_standardUnits = 'BTC'
    oracleUnits_per_standardUnit = 1000000
    public_key = PublicKey('03c22127c967bb28ec518fcc225164100df40470a1f6b457cd3a85adb051dcaa56')


class CnyEM2Beta(OracleUnit):
    name_of_oracleUnits = 'CNY(e-2)'
    name_of_standardUnits = 'CNY'
    oracleUnits_per_standardUnit = 100
    public_key = PublicKey('03c5e3e6a2fe9ed9be3c71a11e7808cf8428bc9ca48808d05a6fa2526865964f06')


class DogeEM1Beta(OracleUnit):
    name_of_oracleUnits = 'DOGE(e-1)'
    name_of_standardUnits = 'DOGE'
    oracleUnits_per_standardUnit = 10
    public_key = PublicKey('0330779426934d4fe5d18a3721e9eae246150501ebc537e866d2841369daeb0691')


class EthEM5Beta(OracleUnit):
    name_of_oracleUnits = 'ETH(e-5)'
    name_of_standardUnits = 'ETH'
    oracleUnits_per_standardUnit = 100000
    public_key = PublicKey('03518d199a4ca5dc06ecb1068416acde321df1b8d6f09149744b1e0fb38c92c92c')


class InrEM0Beta(OracleUnit):
    name_of_oracleUnits = 'INR'
    name_of_standardUnits = 'INR'
    oracleUnits_per_standardUnit = 1
    public_key = PublicKey('03994dc2c759375e98afbf5049383cd987001c346d0f11aa262c105874fb1390c3')


class UsdEM2Beta(OracleUnit):
    name_of_oracleUnits = 'USD(e-2)'
    name_of_standardUnits = 'USD'
    oracleUnits_per_standardUnit = 100
    public_key = PublicKey('02d3c1de9d4bc77d6c3608cbe44d10138c7488e592dc2b1e10a6cf0e92c2ecb047')


class UsdEM2Testing(OracleUnit):
    name_of_oracleUnits = 'USD(e-2)'
    name_of_standardUnits = 'USD'
    oracleUnits_per_standardUnit = 100
    public_key = PublicKey('03e4a5b4a1d9365492dfcad9a05adcdea259acb51a20eabb84584f7aa3c7009ebe')


class XagEM3Beta(OracleUnit):
    name_of_oracleUnits = 'XAG(e-3)'
    name_of_standardUnits = 'XAG'
    oracleUnits_per_standardUnit = 1000
    public_key = PublicKey('03e9342b4d07dc35db0f555b80e19645b2a2a95a22675b50ead248d551a900fdec')


class XauEM5Beta(OracleUnit):
    name_of_oracleUnits = 'XAU(e-5)'
    name_of_standardUnits = 'XAU'
    oracleUnits_per_standardUnit = 100000
    public_key = PublicKey('03e980928f14fc98e1f9d75d15f0b67dc58cdd3f5c641b8f825b146bcc04bd232c')


known_unit_classes = [BtcEM6Beta, CnyEM2Beta, DogeEM1Beta, EthEM5Beta, InrEM0Beta, UsdEM2Beta, UsdEM2Testing, XagEM3Beta, XauEM5Beta]
oracle_pubkey_to_unit_class: dict[PublicKey, Type[OracleUnit]] = {
    u.public_key: u
    for u in known_unit_classes
}


def parse_oracle_price_message(msg_hex: str) -> tuple[ScriptTimestamp, int, int, ScriptPriceInOracleUnitsPerBch]:
    """
    [0, 8) timestamp (4 bytes)
    [8, 16) message sequence (4 bytes)
    [16, 24) price sequence (4 bytes)
    [24, 32) price (4 bytes)
    """
    if len(msg_hex) != 32:
        raise ValueError(f'wrong byte-length ({len(msg_hex)/2}) for a price message (16)')

    # timestamp, msg_sequence, price_sequence/metadatatype should always parse and be valid
    timestamp = ScriptTimestamp(_parse_as_little_endian_signed_int(msg_hex[0:8]))
    msg_sequence = _parse_as_little_endian_signed_int(msg_hex[8:16])
    price_sequence = _parse_as_little_endian_signed_int(msg_hex[16:24])

    if price_sequence == 0:
        raise RuntimeError('this message is out of specification with price sequence == 0')
    elif price_sequence < 0:
        raise ValueError('this is a metadata message, not a price message')

    # Price should always parse and be valid if we get to this point. Unspecified error if not.
    price = ScriptPriceInOracleUnitsPerBch(_parse_as_little_endian_signed_int(msg_hex[24:]))

    return timestamp, msg_sequence, price_sequence, price


def _swap_hex_endianness(data_hex: str) -> str:
    data_bytes = bytearray.fromhex(data_hex)
    data_bytes.reverse()
    data_hex_reversed = ''.join(format(x, '02x') for x in data_bytes)
    return data_hex_reversed


def _parse_as_little_endian_signed_int(data_hex: str) -> int:
    data_bin = decode(data_hex, 'hex_codec')
    value = int.from_bytes(data_bin, byteorder='little', signed=True)
    return value
