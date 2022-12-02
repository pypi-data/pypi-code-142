from enum import Enum

__NAMESPACE__ = "https://eml.ecoinformatics.org/spatialRaster-2.2.0"


class ImagingConditionCode(Enum):
    BLURREDIMAGE = "blurredimage"
    CLOUD = "cloud"
    DEGRADING_OBLIQUITY = "degradingObliquity"
    FOG = "fog"
    HEAVY_SMOKEOR_DUST = "heavySmokeorDust"
    NIGHT = "night"
    RAIN = "rain"
    SEMI_DARKNESS = "semiDarkness"
    SHADOW = "shadow"
    SNOW = "snow"
    TERRAIN_MASKING = "terrainMasking"
