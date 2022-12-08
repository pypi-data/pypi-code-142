import functools

import sqlalchemy
from sqlalchemy import orm

from .models import Submission, Base, PuzzleInput

__all__ = ["Submission", "Base", "PuzzleInput"]


@functools.cache
def get_sessionmaker(uri: str) -> orm.sessionmaker[orm.Session]:
    """Get the database engine.

    :param uri: The database URI
    :return: The database engine
    """
    engine = sqlalchemy.create_engine(uri)
    Base.metadata.create_all(bind=engine)
    return orm.sessionmaker(engine)
