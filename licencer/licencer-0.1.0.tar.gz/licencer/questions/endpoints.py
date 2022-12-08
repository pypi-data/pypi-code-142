from typing import List

from fastapi import APIRouter, Depends, status

from be.errors.exceptions import ApiExceptionFactory
from be.questions.schemas import QuestionApiRequest, QuestionApiResponse
from be.questions.services import QuestionService

router = APIRouter(prefix="/questions", tags=["questions"])


def exception_factory() -> ApiExceptionFactory:
    return ApiExceptionFactory("question")


@router.get("/", response_model=List[QuestionApiResponse])
async def list_all(service: QuestionService = Depends(QuestionService)):
    return await service.find_all()


@router.get("/{question_id}", response_model=QuestionApiResponse)
async def get_by_id(
    question_id: int,
    service: QuestionService = Depends(QuestionService),
    exceptions: ApiExceptionFactory = Depends(exception_factory),
):
    question = await service.find(question_id=question_id)
    if question is not None:
        return question
    else:
        raise exceptions.not_found(question_id)


@router.post(
    "/", response_model=QuestionApiResponse, status_code=status.HTTP_201_CREATED
)
async def create(
    request: QuestionApiRequest, service: QuestionService = Depends(QuestionService)
):
    return await service.create(request=request)
