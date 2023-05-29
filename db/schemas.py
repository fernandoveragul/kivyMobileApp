from pydantic import BaseModel, Field


class SName(BaseModel):
    game_id: int = Field(...)
    name: str = Field(default='name')

    class Config:
        orm_mode = True


class SExample(BaseModel):
    example_id: int = Field(...)
    id_game: int = Field(...)

    class Config:
        orm_mode = True


class SQuestion(BaseModel):
    question_id: int = Field(...)
    text_question: str = Field(default='question')
    tip: str = Field(default='tip')
    id_example: int = Field(...)

    class Config:
        orm_mode = True


class SAnswers(BaseModel):
    answers_id: int = Field(...)
    question: str = Field(default='question')
    first_answer: str = Field(default='first_answer')
    second_answer: str | None = Field(default=None)
    third_answer: str | None = Field(default=None)
    four_answer: str | None = Field(default=None)

    class Config:
        orm_mode = True


class STrueAnswers(BaseModel):
    true_answers_id: int = Field(...)
    question: str = Field(default='question')
    first_answer: str = Field(default='first_answer')
    second_answer: str | None = Field(default=None)
    third_answer: str | None = Field(default=None)
    four_answer: str | None = Field(default=None)

    class Config:
        orm_mode = True
