import sqlite3


class DataBaseInteractor:

    def __init__(self, db_name):
        self._db_name = db_name
        try:
            with sqlite3.connect(self._db_name) as con:
                cur = con.cursor()
                cur.execute("""CREATE TABLE IF NOT EXISTS tasks (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   title TEXT,
                   contents TEXT,
                   datetime TEXT,
                   completed INTEGER
                   )""")
        except Exception as e:
            raise ConnectionError(f'Не удалось создать таблицу. Ошибка {e}')

    def get_from_database(self) -> list:
        try:
            with sqlite3.connect(self._db_name) as con:
                cur = con.cursor()
                cur.execute("""SELECT * FROM tasks""")
                res = cur.fetchall()
                return res
        except Exception as e:
            raise ConnectionError(f'Не удалось получить данные из БД. Ошибка:{e}')

    def add_to_database(self, title: str, contents: str, dt: str, completed: str) -> None:
        try:
            with sqlite3.connect(self._db_name) as con:
                cur = con.cursor()
                cur.execute("""INSERT INTO tasks (title, contents, datetime, completed) \
                VALUES (?, ?, ?, ?)""", (title, contents, dt, completed))
        except Exception as e:
            raise ConnectionError(f'Не удалось записать данные в БД. Ошибка: {e}')

    def change_task_status(self, task_id):
        try:
            with sqlite3.connect(self._db_name) as con:
                cur = con.cursor()
                query = "UPDATE tasks SET completed = 'Выполнено' WHERE id = ?"
                cur.execute(query, (task_id,))
                con.commit()
        except Exception as e:
            raise ConnectionError(f'Не удалось изменить данные в БД. Ошибка: {e}')

    def delete_task(self, task_id):
        try:
            with sqlite3.connect(self._db_name) as con:
                cur = con.cursor()
                query = "DELETE FROM tasks WHERE id = ?"
                cur.execute(query, (task_id,))
                con.commit()
        except Exception as e:
            raise ConnectionError(f'Не удалось изменить данные в БД. Ошибка: {e}')