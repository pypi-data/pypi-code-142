from enum import Enum
from typing import Optional
from uuid import UUID

from serenity_types.utils.serialization import CamelModel


class AssetType(Enum):
    """
    Simple classification of assets.
    """

    CURRENCY = 'CURRENCY'
    """
    Fiat currency, e.g. EUR.
    """

    TOKEN = 'TOKEN'
    """
    Generic tokenized assets.
    """

    PEGGED_TOKEN = 'PEGGED_TOKEN'
    """
    A tokenized asset whose price is linked to an exposure.
    """

    WRAPPED_TOKEN = 'WRAPPED_TOKEN'
    """
    A tokenized asset which represents a claim on a token, typically on another Network.
    """

    FUTURE = 'FUTURE'
    """
    An exchange-listed futures contract.
    """

    LISTED_OPTION = 'LISTED_OPTION'
    """
    An exchange-listed option.
    """

    OTC_OPTION = 'OTC_OPTION'
    """
    An OTC option contract.
    """

    INDEX = 'INDEX'
    """
    A basket of other assets.
    """

    STRATEGY = 'STRATEGY'
    """
    A multi-leg asset composed of positions in other assets.
    """


class Asset(CamelModel):
    """
    Base class for all financial assets tracked in Serenity.
    """

    asset_id: UUID
    """
    Unique, immutable ID for this asset. Symbols can change over time,
    but asset ID's are stable.
    """

    asset_type: AssetType
    """
    Basic classification of this asset. Based on the type, sub-classes of
    the Asset may carry additional details.
    """

    symbol: str
    """
    Serenity's unique symbol for this asset, e.g. tok.usdc.ethereum.
    """

    native_symbol: Optional[str]
    """
    Whatever is the issuer's symbol for this asset. For tokens this is typically the token smart contract symbol
    or native blockchain token symbol, e.g. ETH or DAI.
    """

    display_name: str
    """
    Human-readable name for this asset.
    """
