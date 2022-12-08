from typing import Type
from sqlalchemy import create_engine

from sqlalchemy.orm import DeclarativeBase, declarative_base, sessionmaker

from be.settings import settings

engine = create_engine(
    url=settings.db_url,
    echo=settings.db_echo,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


async def get_db():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


Base: Type[DeclarativeBase] = declarative_base()
