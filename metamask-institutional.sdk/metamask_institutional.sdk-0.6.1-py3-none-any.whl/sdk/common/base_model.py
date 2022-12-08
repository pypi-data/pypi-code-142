from pydantic import BaseModel as PydanticBaseModel


class BaseModel(PydanticBaseModel):
    """
    Configure globally the behaviour of pydantic.

    @see https://pydantic-docs.helpmanual.io/usage/model_config/#change-behaviour-globally
    """
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
