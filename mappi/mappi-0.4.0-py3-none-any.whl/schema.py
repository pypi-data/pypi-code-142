from enum import Enum
from http import HTTPStatus
from typing import Any, Dict, Optional

from pydantic import BaseModel, Field, root_validator
from pydantic.fields import ModelField


class Model(BaseModel):
    @classmethod
    def add_fields(cls, **field_definitions: Any):
        new_fields: Dict[str, ModelField] = {}
        new_annotations: Dict[str, Optional[type]] = {}

        for f_name, f_def in field_definitions.items():
            if isinstance(f_def, tuple):
                try:
                    f_annotation, f_value = f_def
                except ValueError as e:
                    raise Exception(
                        "field definitions should either be a tuple of "
                        "(<type>, <default>) or just a "
                        "default value, unfortunately this means tuples as "
                        "default values are not allowed"
                    ) from e
            else:
                f_annotation, f_value = None, f_def

            if f_annotation:
                new_annotations[f_name] = f_annotation

            new_fields[f_name] = ModelField.infer(
                name=f_name,
                value=f_value,
                annotation=f_annotation,
                class_validators=None,
                config=cls.__config__,
            )

        cls.__fields__.update(new_fields)
        cls.__annotations__.update(new_annotations)

    @classmethod
    def add_route_types(cls):
        for route_type in RouteType:
            field = route_type.value
            if hasattr(cls, field):
                # NOTE: add prefix for reserved fields like `json`
                field_name = f"{field}_data"
                cls.add_fields(**{field_name: (Optional[str], Field(alias=field))})
            else:
                cls.add_fields(**{field: (Optional[str], None)})


class RouteType(str, Enum):
    # BODY = "body"
    HTML = "html"
    JSON = "json"
    TEXT = "text"
    FILE = "file"


class Route(Model):
    path: str
    status: int = HTTPStatus.OK

    route_type: Optional[RouteType]

    @root_validator(pre=True)
    def check_route_type_present(cls, values):
        present_counter: int = 0
        route_type = None
        for r_type in RouteType:
            if r_type.value in values:
                route_type = r_type
                present_counter += 1

        if present_counter == 0:
            raise ValueError("Path type should be specified")

        if present_counter > 1:
            raise ValueError("Found more than one path type")

        # Finally set `route_type` field
        values["route_type"] = route_type
        return values


Route.add_route_types()


class ServerConfig(BaseModel):
    port: int = 5858


class Config(BaseModel):
    server: Optional[ServerConfig] = ServerConfig()
    routes: list[Route]
