from pydantic import BaseModel, Field

from datagen.api.assets.computational import Point, Rotation
from datagen.api.assets.types import LightType
from datagen.config.config import settings

light = settings.assets.light


class Light(BaseModel):
    light_type: LightType
    beam_angle: float = Field(
        title="Beam angle",
        description="Angle of the top of the lightning cone",
        default=light.beam_angle.default,
        ge=light.beam_angle.min,
        le=light.beam_angle.max,
    )
    brightness: float = Field(
        title="Light brightness",
        description="General intensity of the light source",
        default=light.brightness.default,
        ge=light.brightness.min,
        le=light.brightness.max,
    )
    falloff: float = Field(
        title="Light falloff",
        description="Light intensity over distance",
        default=light.falloff.default,
        ge=light.falloff.min,
        le=light.falloff.max,
    )
    location: Point = Field(
        default_factory=lambda: Point(
            x=light.location.x.default, y=light.location.y.default, z=light.location.z.default
        )
    )
    rotation: Rotation = Field(
        default_factory=lambda: Rotation(
            yaw=light.rotation.yaw.default, pitch=light.rotation.pitch.default, roll=light.rotation.roll.default
        )
    )
