import sqlite3
from _config import DATABASE_PATH

with sqlite3.connect(DATABASE_PATH) as connection:
    c = connection.cursor()

    c.execute("""CREATE TABLE tasks(task_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL, due_date TEXT NOT NULL, prioritiy INTEGER NOT NULL,
        status INTEGER NOT NULL)""")

    c.execute('INSERT INTO tasks (name, due_date, prioritiy, status)'
        'VALUES("Finish Real Python Course 2", "02/28/2018", 10, 1)')
