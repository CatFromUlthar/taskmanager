import sqlite3


class DataBaseInteractor:

    def __init__(self, db_name):
        self.db_name = db_name
        try:
            with sqlite3.connect(self.db_name) as con:
                cur = con.cursor()
                cur.execute("""CREATE TABLE IF NOT EXISTS tasks (
                   title TEXT,
                   contents TEXT,
                   datetime TEXT,
                   completed INTEGER
                   )""")
        except Exception as e:
            raise ConnectionError(f'Не удалось создать таблицу. Ошибка {e}')

    def get_from_database(self) -> list:
        try:
            with sqlite3.connect(self.db_name) as con:
                cur = con.cursor()
                cur.execute("""SELECT * FROM tasks""")
                res = cur.fetchall()
                return res
        except Exception as e:
            raise ConnectionError(f'Не удалось получить данные из БД. Ошибка:{e}')

    def add_to_database(self, title: str, contents: str, datetime: str, completed: bool) -> None:
        try:
            with sqlite3.connect(self.db_name) as con:
                cur = con.cursor()
                cur.execute("""INSERT INTO tasks VALUES (?, ?, ?, ?)""", (title, contents, datetime, completed))
        except Exception as e:
            raise ConnectionError(f'Не удалось записать данные в БД. Ошибка: {e}')
