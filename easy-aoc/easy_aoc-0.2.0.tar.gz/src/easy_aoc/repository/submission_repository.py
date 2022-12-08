import contextlib

import attrs
from sqlalchemy import exc, orm

from .. import db, domain, utils


@attrs.define
class SubmissionRepository:
    """A submission repository."""

    sessionmaker: orm.sessionmaker[orm.Session]

    def add(self, submission: domain.Submission) -> None:
        """Add a submission to the database.

        Note: If this submission already exists in the database, no
        additional rows will be written.

        :param submission: The submission to persist
        """
        answer = submission.answer
        with self.sessionmaker() as session:
            session.add(
                db.Submission(**utils.serialize(answer), result=submission.result)
            )
            with contextlib.suppress(exc.IntegrityError):
                session.commit()

    def get(self, answer: domain.Answer) -> domain.Submission | None:
        """Get the cached submission for the answer.

        :param answer: The answer that was submitted
        :return: If found, the cached submission, None otherwise
        """
        with self.sessionmaker() as session:
            query = session.query(db.Submission).filter_by(**utils.serialize(answer))
            submission = query.one_or_none()

        if submission is None:
            return submission

        return domain.Submission(answer=answer, result=submission.result)

    def get_correct_answer(self, part: domain.PuzzlePart) -> domain.Submission | None:
        """Get the correct answer for a puzzle part.

        :param year: The year of the puzzle
        :param day: The day of the puzzle
        :param part: The part of the puzzle
        :return: the correct submission if found, none otherwise
        """
        with self.sessionmaker() as session:
            query = session.query(db.Submission).filter_by(
                **utils.serialize(part), result=domain.Result.CORRECT
            )
            submission = query.one_or_none()

        if submission is None:
            return None

        answer = domain.Answer(part=part, answer=submission.answer)
        return domain.Submission(answer=answer, result=domain.Result.CORRECT)
