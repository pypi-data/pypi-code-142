import os

basedir = os.path.abspath(os.path.dirname(__file__))
postgres_local_base = os.getenv("FRA_DB_URL","postgresql://postgres:@localhost/")
database_name = os.getenv("FRA_DB_NAME","content_based_data")


class BaseConfig:
    """Base configuration."""

    SECRET_KEY = os.getenv("FRA_SECRET_KEY", "my_precious")
    DEBUG = False
    BCRYPT_LOG_ROUNDS = 13
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CELERY_BROKER_URL = os.getenv("FRA_CELERY_BROKER", "redis://localhost:6379/0")
    CELERY_RESULT_BACKEND = os.getenv("FRA_CELERY_BACKEND", "redis://localhost:6379/0")


class DevelopmentConfig(BaseConfig):
    """Development configuration."""

    DEBUG = True
    BCRYPT_LOG_ROUNDS = 4
    SQLALCHEMY_DATABASE_URI = postgres_local_base + database_name


class TestingConfig(BaseConfig):
    """Testing configuration."""

    DEBUG = True
    TESTING = True
    BCRYPT_LOG_ROUNDS = 4
    SQLALCHEMY_DATABASE_URI = postgres_local_base + database_name + "_test"
    PRESERVE_CONTEXT_ON_EXCEPTION = False


class ProductionConfig(BaseConfig):
    """Production configuration."""

    SECRET_KEY = os.getenv("FRA_SECRET_KEY", "my_precious")
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv("FRA_DB_URI", None)
