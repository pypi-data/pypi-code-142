import sqlalchemy
from sqlalchemy import orm

from easy_aoc import domain


class Base(orm.DeclarativeBase):
    """The declarative base for all ORM models."""


class PuzzleInput(Base):
    __tablename__ = "puzzle_input"

    year: orm.Mapped[int] = orm.mapped_column(sqlalchemy.SmallInteger, primary_key=True)
    day: orm.Mapped[int] = orm.mapped_column(sqlalchemy.SmallInteger, primary_key=True)
    text: orm.Mapped[str] = orm.mapped_column(sqlalchemy.Text, nullable=False)


class Submission(Base):
    __tablename__ = "answer"
    __table_args__ = (sqlalchemy.UniqueConstraint("year", "day", "part", "answer"),)

    id: orm.Mapped[int] = orm.mapped_column(sqlalchemy.Integer, primary_key=True)
    year: orm.Mapped[int] = orm.mapped_column(sqlalchemy.SmallInteger, nullable=False)
    day: orm.Mapped[int] = orm.mapped_column(sqlalchemy.SmallInteger, nullable=False)
    part: orm.Mapped[int] = orm.mapped_column(sqlalchemy.SmallInteger, nullable=False)
    answer: orm.Mapped[str] = orm.mapped_column(
        sqlalchemy.String(length=64), nullable=False
    )
    result: orm.Mapped[domain.Result] = orm.mapped_column(
        sqlalchemy.Enum(domain.Result), nullable=False
    )
