from typing import Sequence

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from be.database import get_db
from be.questions.models import Question


class QuestionRepository:
    def __init__(self, db: Session = Depends(get_db)):
        self._db = db

    async def save(self, question: Question) -> Question:
        self._db.add(question)
        self._db.commit()
        self._db.refresh(question)
        return question

    async def find_by_id(self, question_id: int) -> Question | None:
        statement = select(Question).filter_by(question_id=question_id)
        result = self._db.execute(statement)
        return result.scalar()

    async def find_all(self) -> Sequence[Question]:
        statement = select(Question)
        result = self._db.execute(statement)
        return result.scalars().all()
