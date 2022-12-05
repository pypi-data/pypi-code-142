from pathlib import Path
from typing import Any, Dict, Optional

from pydantic.class_validators import validator
from pydantic.env_settings import BaseSettings
from pydantic.networks import AnyHttpUrl


class ElasticSearchSettings(BaseSettings):
    ES_HOST: str = 'localhost'
    ES_PORT: int = 9200
    ES_USER: str = 'elastic'
    ES_PASSWORD: str = 'elastic'
    ES_PASSWORD_FILE: Optional[Path] = None

    ES_URI: Optional[AnyHttpUrl] = None

    @validator('ES_URI', pre=True)
    def assemble_es_connection(cls, v: Optional[str], values: Dict[str, Any]) -> str:
        if isinstance(v, str):
            return v

        if 'ES_PASSWORD_FILE' in values:
            password_file = values.get('ES_PASSWORD_FILE')
            if isinstance(password_file, Path) and password_file.exists():
                with password_file.open() as f:
                    values['ES_PASSWORD'] = f.read().strip()

        return f'http://{values.get("ES_USER")}:{values.get("ES_PASSWORD")}' \
               f'@{values.get("ES_HOST")}:{values.get("ES_PORT")}/'

    class Config:
        case_sensitive = False
        env_file = '.env'
