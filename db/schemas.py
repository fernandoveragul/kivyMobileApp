from dataclasses import dataclass


@dataclass
class SGame:
    name: str


@dataclass
class SExample:
    name: str
    name_game: str


@dataclass
class SQuestion:
    text_question: str
    tip: str
    name_example: int


@dataclass
class SAnswers:
    answers_id: int
    answers: str
    name_field_answer: str
    question: str


def get_schema(schema_name: str):
    match schema_name:
        case 'game':
            return SGame
        case 'example':
            return SExample
        case 'question':
            return SQuestion
        case 'answer':
            return SAnswers
