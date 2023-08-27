# Знайти студента із найвищим середнім балом з певного предмета.
import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('data.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
SELECT ROUND(AVG(r.assessment), 2) AS average, s.students_name                    
FROM ratings AS r
LEFT JOIN students as s ON r.student_id = s.id
WHERE subject_id = 1
GROUP BY student_id
ORDER BY average DESC
LIMIT 1;
"""

print(execute_query(sql))