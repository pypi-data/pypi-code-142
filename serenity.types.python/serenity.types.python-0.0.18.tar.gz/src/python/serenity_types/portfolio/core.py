from uuid import UUID


class AssetPosition:
    """
    A simple representation of holding a certain amount of a given asset.
    This is going to be replaced with a much more flexible Portfolio
    representation in Q1'23.
    """

    asset_id: UUID
    """
    Unique identifier of the asset from Serenity's asset master database.
    """

    quantity: float
    """
    The number of tokens, shares, contracts, etc. held in this position.
    If positive this indicates a long position; if negative, a short one.
    """
