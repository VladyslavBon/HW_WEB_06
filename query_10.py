# Список курсів, які певному студенту читає певний викладач.
import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('data.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
SELECT sj.subjects_name                    
FROM subjects AS sj
LEFT JOIN ratings as r ON sj.id = r.subject_id
WHERE student_id = 1 and teacher_id = 1
GROUP BY subject_id
"""

print(execute_query(sql))