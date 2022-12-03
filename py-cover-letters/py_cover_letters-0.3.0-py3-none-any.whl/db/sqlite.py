from pathlib import Path

from sqlalchemy.exc import NoResultFound
from sqlmodel import create_engine, SQLModel, Session, select

from .models import CoverLetter
from ..enums import FilterType  # type: ignore
from ..exceptions import UnsupportedOperationException  # type: ignore


class CoverLetterManager:

    def __init__(self, sql_file: Path):
        self.engine = create_engine(f'sqlite:///{sql_file}')
        SQLModel.metadata.create_all(self.engine)  # , tables=[CoverLetter])

    def _exec(self, statement):
        with Session(self.engine) as session:
            project_result = session.exec(statement)

            return project_result

    def get(self, cover_letter_id: int) -> CoverLetter:
        try:
            with Session(self.engine) as session:
                statement = select(CoverLetter).where(CoverLetter.id == cover_letter_id)
                results = session.exec(statement)
                db_project = results.one()
            return db_project
        except NoResultFound:
            return None

    def create(self, cover_letter: CoverLetter):
        with Session(self.engine) as session:
            session.add(cover_letter)
            session.commit()
            session.refresh(cover_letter)
        return cover_letter

    def delete(self, cover_letter: CoverLetter):
        with Session(self.engine) as session:
            statement = select(CoverLetter).where(CoverLetter.id == cover_letter.id)
            results = session.exec(statement)
            db_project = results.one()
            session.delete(db_project)
            session.commit()
        return cover_letter

    def update(self, project: CoverLetter):
        with Session(self.engine) as session:
            statement = select(CoverLetter).where(CoverLetter.id == project.id)
            results = session.exec(statement)
            db_project = results.one()
            exclude = ['id', 'created']
            project_dict = project.dict()
            for key, value in project_dict.items():
                if key not in exclude:
                    setattr(db_project, key, value)
            session.add(db_project)
            session.commit()
            session.refresh(db_project)

    def list(self):
        with Session(self.engine) as session:
            statement = select(CoverLetter)
            cover_letters = session.exec(statement).all()
            return cover_letters

    def filter(self, filter_type: FilterType):
        with Session(self.engine) as session:
            if filter_type == FilterType.COVER_LETTER_NOT_CREATED:
                statement = select(CoverLetter).where(CoverLetter.date_generated == None)  # noqa
            elif filter_type == FilterType.COVER_LETTER_NOT_DELETED:
                statement = select(CoverLetter).where(CoverLetter.delete == False)  # noqa
            else:
                error_message = f'Filter type {filter_type} is not currently supported.'
                raise UnsupportedOperationException(error_message)
            cover_letters = session.exec(statement).all()
            return cover_letters

