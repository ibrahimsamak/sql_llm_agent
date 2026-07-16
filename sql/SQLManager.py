import sqlite3

class SQLManager:
    def __init__(self):
        self.conn = sqlite3.connect('school.db')
        self.cursor = self.conn.cursor()

    
    def create_student_table(self):
        create_tbl_student = """
            CREATE TABLE IF NOT EXISTS students (
                student_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER
            )
            """
        self.cursor.execute(create_tbl_student)
    

    def create_subject_table(self):
        create_tbl_subject = """
            CREATE TABLE IF NOT EXISTS subjects (
                subject_id INTEGER PRIMARY KEY AUTOINCREMENT,
                subject_name TEXT NOT NULL
            )
            """
        self.cursor.execute(create_tbl_subject)

    def create_student_subject_mark_table(self):
        create_tbl_student_subject = """
        CREATE TABLE IF NOT EXISTS student_marks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER,
            subject_id INTEGER,
            mark INTEGER,
            FOREIGN KEY(student_id) REFERENCES students(student_id),
            FOREIGN KEY(subject_id) REFERENCES subjects(subject_id)
        )
        """
        self.cursor.execute(create_tbl_student_subject)

    def main(self):
        self.create_student_table()
        self.create_subject_table()
        self.create_student_subject_mark_table()


app = SQLManager()
