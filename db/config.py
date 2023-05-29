from pathlib import Path

from sqlalchemy import create_engine
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
