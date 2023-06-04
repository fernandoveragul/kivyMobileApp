import sqlite3
from sqlite3 import Connection
from pathlib import Path


def get_connection() -> Connection:
    with sqlite3.connect(f"{Path(Path.cwd(), 'db', 'db.sqlite')}") as connection:
        return connection
