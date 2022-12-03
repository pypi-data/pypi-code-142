"""
Define a entidade de Categoria
"""
# Python
from typing import Any, Dict, Optional
from datetime import datetime
from dataclasses import field, dataclass

# Third
from slugify import slugify

# Apps
from kernel_catalogo_videos.core.utils import ACTIVE_STATUS, INACTIVE_STATUS, now
from kernel_catalogo_videos.core.domain.entities import Entity

# from kernel_catalogo_videos.core.domain.exceptions import EntityValidationException

# from kernel_catalogo_videos.categories.domain.factories import CategoryValidatorFactory


@dataclass(kw_only=True, frozen=True, slots=True)
class Category(Entity):
    """
    Representa a entidade categoria e seus dados
    """

    title: str
    slug: Optional[str] = ""
    description: Optional[str] = ""
    status: Optional[int] = ACTIVE_STATUS
    is_deleted: bool = False
    created_at: Optional[datetime] = field(default_factory=now)

    def __post_init__(self):
        # slug title
        self.normalize()

    def update(self, data: Dict[str, Any]):
        """
        Atualiza os dados internos da entidade
        """
        for field_name, value in data.items():
            self._set(field_name, value)

        self.normalize()
        # self.validate()

    def _set(self, field_name, value):
        object.__setattr__(self, field_name, value)

        return self

    def activate(self):
        """
        Seta o atributo status como ativo
        """
        self._set("status", ACTIVE_STATUS)

    def deactivate(self):
        """
        Seta o atributo status como inativo
        """
        self._set("status", INACTIVE_STATUS)

    def normalize(self):
        slugged = slugify(self.title)
        self._set("slug", slugged)

    # def validate(self, serializer_class):
    #     """
    #     Instancia um validador e executa o metodo validate
    #     """
    #     validator = CategoryValidatorFactory.create(serializer_class=serializer_class)
    #     is_valid = validator.validate(data=self.to_dict())
    #     if not is_valid:
    #         raise EntityValidationException(validator.errors)
