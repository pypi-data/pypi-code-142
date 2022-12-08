from typing import Optional

from pydantic import Field

from datagen.api.assets.base import DatapointRequestAsset
from datagen.api.assets.human.expression import Expression
from datagen.api.assets.human.eyes import Eyes
from datagen.api.assets.human.hair import Hair
from datagen.api.assets.computational import Point, Rotation
from datagen.config import settings

head = settings.assets.head


class Head(DatapointRequestAsset):
    eyes: Eyes
    hair: Optional[Hair]
    eyebrows: Optional[Hair]
    facial_hair: Optional[Hair]
    location: Point = Field(
        default_factory=lambda: Point(x=head.location.x.default, y=head.location.y.default, z=head.location.z.default)
    )
    rotation: Rotation = Field(
        default_factory=lambda: Rotation(
            yaw=head.rotation.yaw.default, pitch=head.rotation.pitch.default, roll=head.rotation.roll.default
        )
    )
    expression: Expression = Field(default_factory=Expression)
