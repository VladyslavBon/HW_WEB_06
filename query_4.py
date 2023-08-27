# Знайти середній бал на потоці (по всій таблиці оцінок).
import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('data.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
SELECT ROUND(AVG(r.assessment), 2)                    
FROM ratings AS r
"""

print(execute_query(sql))