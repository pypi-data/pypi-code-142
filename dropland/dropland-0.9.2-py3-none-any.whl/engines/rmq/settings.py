from pathlib import Path
from typing import Any, Dict, Optional

from pydantic.class_validators import validator
from pydantic.env_settings import BaseSettings
from pydantic.networks import AmqpDsn


class RmqSettings(BaseSettings):
    RMQ_HOST: str = 'localhost'
    RMQ_PORT: int = 5672
    RMQ_USER: str = 'guest'
    RMQ_PASSWORD: str = 'guest'
    RMQ_PASSWORD_FILE: Optional[Path] = None
    RMQ_VIRTUALHOST: str = '/'
    RMQ_TIMEOUT_SECONDS: int = 5
    RMQ_POOL_MAX_CONNECTIONS: int = 4
    RMQ_POOL_MAX_CHANNELS_PER_CONNECTION: int = 100

    RMQ_URI: Optional[AmqpDsn] = None

    @validator('RMQ_URI', pre=True)
    def assemble_rmq_connection(cls, v: Optional[str], values: Dict[str, Any]) -> str:
        if isinstance(v, str):
            return v

        if 'RMQ_PASSWORD_FILE' in values:
            password_file = values.get('RMQ_PASSWORD_FILE')
            if isinstance(password_file, Path) and password_file.exists():
                with password_file.open() as f:
                    values['RMQ_PASSWORD'] = f.read().strip()

        return AmqpDsn.build(
            scheme='amqp',
            user=values.get('RMQ_USER'),
            password=values.get('RMQ_PASSWORD'),
            host=values.get('RMQ_HOST'),
            port=str(values.get('RMQ_PORT')),
        )

    class Config:
        case_sensitive = False
        env_file = '.env'
