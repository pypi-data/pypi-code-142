"""
Define uma entidade
"""
# Python
from typing import Optional
from datetime import datetime
from dataclasses import field, dataclass

# Apps
from kernel_catalogo_videos.core.utils import ACTIVE_STATUS, now
from kernel_catalogo_videos.core.domain.entities import Entity


@dataclass(kw_only=True, frozen=True, slots=True)
class Genre(Entity):
    """
    Representa os dados da entidade genero
    """

    title: str
    slug: str
    status: Optional[int] = ACTIVE_STATUS
    is_deleted: bool = False
    created_at: Optional[datetime] = field(default_factory=now)
