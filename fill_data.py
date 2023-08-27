from datetime import datetime
import faker
from random import randint
import sqlite3

NUMBER_STUDENTS = 30
NUMBER_TEACHERS = 3
GROUPS = [('First group',), ('Second_group',), ('Third group',)]
SUBJECTS = ['Math', 'Physics', 'Ukrainian', 'English', 'Сhemistry']


def generate_fake_data(number_students, number_teachers) -> tuple():
    fake_students = []
    fake_teachers = []
    fake_data = faker.Faker()

    for _ in range(number_students):
        fake_students.append(fake_data.name())

    for _ in range(number_teachers):
        fake_teachers.append(fake_data.name())

    return fake_students, fake_teachers


def prepare_data(students, teachers) -> tuple():
    for_groups = GROUPS

    for_students = []

    for student in students:
        for_students.append((student, randint(1, len(GROUPS))))

    for_teachers = []

    for teacher in teachers:
        for_teachers.append((teacher, ))

    for_subjects = []

    for subject in SUBJECTS:
        for_subjects.append((subject, randint(1, NUMBER_TEACHERS)))

    for_ratings = []

    for month in range(1, 12 + 1):
        assessment_date = datetime(2022, month, randint(20, 25)).date()
        for student in range(1, NUMBER_STUDENTS + 1):
            for_ratings.append((student, randint(1, len(SUBJECTS)), randint(1, 100), assessment_date))

    return for_groups, for_students, for_teachers, for_subjects, for_ratings


def insert_data_to_db(groups, students, teachers, subjects, ratings) -> None:

    with sqlite3.connect('data.db') as con:
        cur = con.cursor()

        sql_to_groups = """INSERT INTO groups(group_name)
                               VALUES (?)"""
        cur.executemany(sql_to_groups, groups)
        

        sql_to_students = """INSERT INTO students(students_name, groups_id)
                               VALUES (?, ?)"""
        cur.executemany(sql_to_students, students)


        sql_to_teachers = """INSERT INTO teachers(teachers_name)
                               VALUES (?)"""
        cur.executemany(sql_to_teachers, teachers)


        sql_to_subjects = """INSERT INTO subjects(subjects_name, teacher_id)
                               VALUES (?, ?)"""
        cur.executemany(sql_to_subjects, subjects)

        
        sql_to_ratings = """INSERT INTO ratings(student_id, subject_id, assessment, date_of)
                              VALUES (?, ?, ?, ?)"""
        cur.executemany(sql_to_ratings, ratings)

        con.commit()


if __name__ == "__main__":
    groups, students, teachers, subjects, ratings = prepare_data(*generate_fake_data(NUMBER_STUDENTS, NUMBER_TEACHERS))
    insert_data_to_db(groups, students, teachers, subjects, ratings)