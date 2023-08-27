# Знайти середній бал, який ставить певний викладач зі своїх предметів.
import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('data.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
SELECT ROUND(AVG(r.assessment), 2) AS average, t.teachers_name                     
FROM ratings AS r
LEFT JOIN teachers as t ON r.subject_id = t.id
WHERE t.id = 1
"""

print(execute_query(sql))