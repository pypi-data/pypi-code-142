from typing import List

from fastapi import Depends

from be.questions.repositories import QuestionRepository
from be.questions.schemas import QuestionApiRequest, QuestionApiResponse


class QuestionService:
    def __init__(self, questions: QuestionRepository = Depends(QuestionRepository)):
        self._questions = questions

    async def find(self, question_id: int) -> QuestionApiResponse | None:
        question = await self._questions.find_by_id(question_id)
        if question is not None:
            return QuestionApiResponse.from_orm(question)
        else:
            return None

    async def find_all(self) -> List[QuestionApiResponse]:
        questions = await self._questions.find_all()
        return [*map(QuestionApiResponse.from_orm, questions)]

    async def create(self, request: QuestionApiRequest) -> QuestionApiResponse:
        question = await self._questions.save(request.to_model())
        return QuestionApiResponse.from_orm(question)
