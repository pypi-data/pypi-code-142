import secrets
from typing import Any, Dict, List, Optional, Union
from pydantic import (
    AnyHttpUrl,
    BaseSettings,
    EmailStr,
    PostgresDsn,
    validator,
    SecretStr,
)


class Settings(BaseSettings):
    ETIKET_TEST: bool
    ETIKET_NAME: str
    ETIKET_SECRET_KEY: str = secrets.token_urlsafe(32)

    ETIKET_ACCESS_TOKEN_EXPIRE_MINUTES: float = 30.0
    ETIKET_REFRESH_TOKEN_EXPIRE_MINUTES: float = 60 * 24 * 30

    ETIKET_UPLOADS_PATH: str
    ETIKET_FILESTORAGE_PATH: str
    ETIKET_FLOW_LOCKS_PATH: str
    ETIKET_MAX_FILE_SIZE: int = 214748364800
    ETIKET_MIN_PARTIAL_FILE_SIZE: int = 10485760
    ETIKET_CHUNK_SIZE: int = 4194304

    ETIKET_TUS_RESUMABLE: str = "1.0.0"
    ETIKET_TUS_CHECKSUM_ALGORITHMS: List[str] = ["md5", "sha1"]
    ETIKET_TUS_EXTENSIONS: List[str] = [
        "creation",
        "creation-with-upload",
        "expiration",
        "checkum",
        "termination",
        "concatenation",
    ]

    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    # for now
    SQLITE_FILE_NAME: str = "database.db"
    SQLITE_URL: str = f"sqlite:///{SQLITE_FILE_NAME}"

    # for when it is the real deal
    POSTGRES_SERVER: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_PORT: int = 5432
    SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn] = None

    @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme="postgresql",
            user=values.get("POSTGRES_USER"),
            password=values.get("POSTGRES_PASSWORD"),
            host=values.get("POSTGRES_SERVER"),
            path=f"/{values.get('POSTGRES_DB') or ''}",
        )

    S3_ENDPOINT: AnyHttpUrl
    S3_PREFIX: str
    S3_BUCKET: str
    S3_ACCESS_KEY_ID: str = None
    S3_SECRET_ACCESS_KEY: SecretStr = None
    S3_SINGLEPART_SIZE_LIMIT: int
    S3_MIN_PART_SIZE: int
    S3_MAX_PART_SIZE: int
    S3_PRESIGN_EXPIRATION: int
    S3_MAX_NUMBER_PARTS: int
    S3_MULTIPART_UPLOAD_PARTSIZE: int
    S3_STREAM_NUMBER_OF_PARTS: int

    ETIKET_ADMIN_USERNAME: str
    ETIKET_ADMIN_PASSWORD: str
    ETIKET_ADMIN_EMAIL: EmailStr

    class Config:
        env_file = ".env"
        env_prefix = ""
        case_sentive = False
        env_file_encoding = "utf-8"


settings = Settings()
