from enum import Enum
from functools import partial
from typing import List, Any, Optional, TypeVar, Type

import marshmallow
import marshmallow_dataclass
from marshmallow_dataclass import NewType
from marshmallow_enum import EnumField

from datagen.api.catalog.cache import InMemAssetCache
from datagen.dev import DescriptiveEnum


Asset = TypeVar("Asset")


EnumType = partial(NewType, "Enum", Enum, EnumField, by_value=True)


class DynamicList(marshmallow.fields.List):
    def _deserialize(self, value, attr, data, **kwargs) -> List[Any]:
        if not isinstance(value, list):
            value = [value]
        return super()._deserialize(value, attr, data, **kwargs)


@marshmallow_dataclass.dataclass
class AssetAttributes:
    class Meta:
        unknown = marshmallow.EXCLUDE


class AssetAttributesSchema(marshmallow.Schema):
    TYPE_MAPPING = {List: DynamicList}


asset_attributes_dataclass = partial(marshmallow_dataclass.dataclass, base_schema=AssetAttributesSchema)


class Ethnicity(DescriptiveEnum):
    AFRICAN = "african"
    SOUTH_ASIAN = "south_asian"
    EAST_ASIAN = "east_asian"
    SOUTHEAST_ASIAN = "southeast_asian"
    HISPANIC = "hispanic"
    MEDITERRANEAN = "mediterranean"
    NORTH_EUROPEAN = "north_european"


class Gender(DescriptiveEnum):
    FEMALE = "female"
    MALE = "male"


class Age(DescriptiveEnum):
    ADULT = "adult"
    OLD = "old"
    YOUNG = "young"


@asset_attributes_dataclass
class HumanAttributes(AssetAttributes):
    age: EnumType(enum=Age)
    ethnicity: EnumType(enum=Ethnicity)
    gender: EnumType(enum=Gender)


class EyesColor(DescriptiveEnum):
    BROWN = "brown"
    GREEN = "green"
    BLUE = "blue"


@asset_attributes_dataclass
class EyesAttributes(AssetAttributesSchema):
    color: EnumType(enum=EyesColor)


class AccessoryPosition(DescriptiveEnum):
    ON_CHIN = "chin"
    ON_MOUTH = "mouth"
    ON_NOSE = "nose"


class GlassesModel(DescriptiveEnum):
    GENERAL = "general"


class GlassesBrand(DescriptiveEnum):
    GENERAL = "general"


class GlassesStyle(DescriptiveEnum):
    AVIATOR = "aviator"
    BROWLINE = "browline"
    CAT_EYE = "cat_eye"
    GEOMETRIC = "geometric"
    OVAL = "oval"
    OVERSIZED = "oversized"
    READING_FULL_FRAME = "reading_full_frame"
    READING_RIMLESS = "reading_rimless"
    ROUND = "round"


@asset_attributes_dataclass
class AccessoryAttributes(AssetAttributes):
    supported_position: List[EnumType(enum=AccessoryPosition)]
    gender: List[EnumType(enum=Gender)]


@asset_attributes_dataclass
class GlassesAttributes(AccessoryAttributes):
    style: EnumType(enum=GlassesStyle)


class MaskStyle(DescriptiveEnum):
    CLOTH = "cloth"


@asset_attributes_dataclass
class MaskAttributes(AccessoryAttributes):
    style: EnumType(enum=MaskStyle)


class HairLength(DescriptiveEnum):
    BUZZ_CUT = "buzz_cut"
    UNDEFINED = "undefined"
    SHOULDER = "shoulder"
    CHIN = "chin"
    ARMPIT = "armpit"
    EAR = "ear"
    TAILBONE = "tailbone"
    MID_BACK = "mid_back"


class HairStyle(DescriptiveEnum):
    LAYERED = "layered"
    UNDEFINED = "undefined"
    HAIR_DOWN = "hair_down"
    BUN = "bun"
    CURTAIN = "curtain"
    BALDING = "balding"
    BANGS = "bangs"
    HIGH_TOP_CUT = "high_top_cut"
    PONYTAIL = "ponytail"
    PULLED_BACK = "pulled_back"
    AFRO = "afro"
    CREW_CUT = "crew_cut"
    BOB = "bob"


@asset_attributes_dataclass
class HairAttributes(AssetAttributes):
    age_group_match: List[EnumType(enum=Age)]
    ethnicity_match: List[EnumType(enum=Ethnicity)]
    gender_match: List[EnumType(enum=Gender)]
    length: EnumType(enum=HairLength)
    style: List[EnumType(enum=HairStyle)]


@asset_attributes_dataclass
class EyebrowsAttributes(AssetAttributes):
    gender_match: List[EnumType(enum=Gender)]


class Environment(DescriptiveEnum):
    INDOOR = "indoor"
    OUTDOOR = "outdoor"
    CROSS_POLARIZED = "cross_polarized"


class TimeOfDay(DescriptiveEnum):
    MORNING = "morning"
    EVENING = "evening"
    NIGHT = "night"
    NA = "N/A"


@asset_attributes_dataclass
class BackgroundAttributes(AssetAttributes):
    environment: EnumType(enum=Environment)
    time_of_day: EnumType(enum=TimeOfDay)
    strength: Optional[float] = None


class BeardStyle(DescriptiveEnum):
    FULL_BEARD = "full_beard"
    STUBBLE = "stubble"
    MUSTACHE = "mustache"
    BEARD = "beard"
    PARTIAL_BEARD = "partial_beard"


@asset_attributes_dataclass
class BeardAttributes(AssetAttributes):
    style: EnumType(enum=BeardStyle)


class AllOf(list):
    def __init__(self, *attributes):
        super().__init__(attributes)


class AnyOf(list):
    def __init__(self, *attributes):
        super().__init__(attributes)


class Exactly(list):
    def __init__(self, *attributes):
        super().__init__(attributes)


class AssetAttributesCache(InMemAssetCache):
    def __init__(self, attributes_type: Type[AssetAttributes], cache_file_name: str):
        super().__init__(cache_provider=attributes_type.Schema().load, cache_file_name=cache_file_name)

    def _is_matching(self, asset_cache_content: AssetAttributes, query_params: dict):
        asset_attributes, query_attributes = asset_cache_content, query_params
        matching = True
        for query_tag_name, query_attribute_vals in query_attributes.items():
            asset_attribute_vals, query_attribute_vals = self._get_attributes_values(
                asset_attributes, query_tag_name, query_attribute_vals
            )
            if isinstance(query_attribute_vals, AllOf):
                matching &= all(v in asset_attribute_vals for v in query_attribute_vals)
            elif isinstance(query_attribute_vals, AnyOf):
                matching &= any(v in asset_attribute_vals for v in query_attribute_vals)
            elif isinstance(query_attribute_vals, Exactly):
                matching &= set(asset_attribute_vals) == set(query_attribute_vals)
        return matching

    @staticmethod
    def _get_attributes_values(
        asset_attributes: AssetAttributes, query_tag_name: str, query_tag_value: object
    ) -> tuple:
        asset_tag_value = getattr(asset_attributes, query_tag_name)
        if not isinstance(query_tag_value, (AllOf, AnyOf, Exactly)):
            query_tag_value = AllOf(query_tag_value)
        if not isinstance(asset_tag_value, list):
            asset_tag_value = [asset_tag_value]
        return asset_tag_value, query_tag_value


def __dir__():
    return [
        "Ethnicity",
        "Gender",
        "Age",
        "BeardStyle",
        "EyesColor",
        "AccessoryPosition",
        "GlassesModel",
        "GlassesBrand",
        "GlassesStyle",
        "MaskStyle",
        "HairLength",
        "HairStyle",
        "Environment",
        "TimeOfDay",
        "AnyOf",
        "AllOf",
        "Exactly",
    ]
