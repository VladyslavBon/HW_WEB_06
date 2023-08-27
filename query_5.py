# Знайти, які курси читає певний викладач.
import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('data.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
SELECT subjects_name
FROM subjects
WHERE teacher_id = 1
ORDER BY subjects_name
"""

print(execute_query(sql))