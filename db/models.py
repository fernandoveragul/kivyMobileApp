from sqlalchemy import Column, Integer, String, ForeignKey

from db.config import Base


class MName(Base):
    __tablename__ = 'game'

    game_id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String, nullable=False)


class MExample(Base):
    __tablename__ = 'example'

    example_id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    id_game = Column(Integer, ForeignKey('game.game_id'))


class MQuestion(Base):
    __tablename__ = 'question'

    question_id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    text_question = Column(String, nullable=False, unique=True)
    tip = Column(String, nullable=True)
    id_example = Column(Integer, ForeignKey('example.example_id'))


class MAnswers(Base):
    __tablename__ = 'answers'

    answers_id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    question = Column(Integer, ForeignKey('question.text_question'))
    first_answer = Column(String, nullable=False)
    second_answer = Column(String, default=None, nullable=True)
    third_answer = Column(String, default=None, nullable=True)
    four_answer = Column(String, default=None, nullable=True)


class MTrueAnswers(Base):
    __tablename__ = 'true_answers'

    true_answers_id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    question = Column(Integer, ForeignKey('question.text_question'))
    first_answer = Column(String, nullable=False)
    second_answer = Column(String, default=None, nullable=True)
    third_answer = Column(String, default=None, nullable=True)
    four_answer = Column(String, default=None, nullable=True)
