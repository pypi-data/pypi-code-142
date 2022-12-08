import typing_extensions

from clothes_sdk_ashuk203.paths import PathValues
from clothes_sdk_ashuk203.apis.paths.tshirts_id import TshirtsId

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.TSHIRTS_ID: TshirtsId,
    }
)

path_to_api = PathToApi(
    {
        PathValues.TSHIRTS_ID: TshirtsId,
    }
)
