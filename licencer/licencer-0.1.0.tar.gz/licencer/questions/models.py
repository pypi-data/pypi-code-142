from typing import cast

from sqlalchemy import Column, Integer, String

from be.database import Base


class Question(Base):
    __tablename__ = "questions"

    question_id = cast(int, Column(Integer, primary_key=True))
    module_id: int = cast(int, Column(Integer))
    content = cast(str, Column(String, name="content_md"))
    difficulty = cast(int, Column(Integer))
