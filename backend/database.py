import sqlite3

DATABASE = "students.db"


def create_table():
    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            attendance REAL NOT NULL,
            internal_marks REAL NOT NULL,
            study_hours REAL NOT NULL,
            assignment_completion REAL NOT NULL
        )
    """)

    connection.commit()
    connection.close()


def add_student(name, attendance, internal_marks, study_hours, assignment_completion):
    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO students
        (name, attendance, internal_marks, study_hours, assignment_completion)
        VALUES (?, ?, ?, ?, ?)
    """, (
        name,
        attendance,
        internal_marks,
        study_hours,
        assignment_completion
    ))

    connection.commit()
    connection.close()