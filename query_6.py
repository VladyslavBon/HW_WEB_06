# Знайти список студентів у певній групі.
import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('data.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
SELECT students_name
FROM students
WHERE groups_id = 1
ORDER BY students_name
"""

print(execute_query(sql))