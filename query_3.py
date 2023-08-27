# Знайти середній бал у групах з певного предмета.
import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('data.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
SELECT ROUND(AVG(r.assessment), 2) as average, g.group_name                     
FROM ratings AS r
LEFT JOIN groups as g ON r.student_id = g.id
WHERE subject_id = 1 and g.id IN(1, 2, 3) 
GROUP BY g.group_name
"""

print(execute_query(sql))