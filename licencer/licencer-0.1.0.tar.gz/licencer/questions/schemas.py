from pydantic import BaseModel

from be.questions.models import Question


class QuestionApiResponse(BaseModel):
    question_id: int
    module_id: int
    difficulty: int
    content: str

    class Config:
        orm_mode = True


class QuestionApiRequest(BaseModel):
    module_id: int = 1
    difficulty: int = 3
    content: str

    def to_model(self) -> Question:
        return Question(
            module_id=self.module_id,
            difficulty=self.difficulty,
            content=self.content,
        )
