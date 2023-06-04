from sqlite3 import Connection, Cursor

from db.config import get_connection
from db.schemas import *


class DB:
    connection: Connection = get_connection()

    @classmethod
    def select(cls, *, table_name: str,
               column_param: str | None = None,
               where_param: str | None = None) -> list[SGame | SExample | SQuestion | SAnswers]:
        statement: str = 'SELECT'
        if column_param is not None:
            statement += f' {column_param} FROM {table_name}'
        else:
            statement += f' * FROM {table_name}'
        if where_param is not None:
            statement += f' WHERE {where_param}'

        cursor: Cursor = cls.connection.execute(statement)
        schema = get_schema(table_name)
        result = [schema(*note) for note in cursor.fetchall()]
        return result
