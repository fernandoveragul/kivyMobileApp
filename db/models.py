from pathlib import Path

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, Session

DB_NAME = "db.sqlite"
DB_URL = f"sqlite:///{Path(Path.cwd(), 'db', DB_NAME)}"

engine = create_engine(url=DB_URL)
db_session = sessionmaker(bind=engine, expire_on_commit=False)
Base = declarative_base()


def get_session() -> Session:
    with db_session() as session:
        return session


def create_all_tables():
    Base.metadata.create_all(engine)


class MGame(Base):
    __tablename__ = 'game'

    name = Column(String, primary_key=True)


class MExample(Base):
    __tablename__ = 'example'

    name = Column(String, primary_key=True)
    name_game = Column(String, ForeignKey('game.name'))


class MQuestion(Base):
    __tablename__ = 'question'

    text_question = Column(String, primary_key=True)
    tip = Column(String, nullable=True)
    name_example = Column(Integer, ForeignKey('example.name'))


class MAnswers(Base):
    __tablename__ = 'answer'

    answers_id = Column(Integer, primary_key=True)
    answer = Column(String, nullable=False, default='answ')
    name_field_answer = Column(String, nullable=False)
    question = Column(Integer, ForeignKey('question.text_question'))
