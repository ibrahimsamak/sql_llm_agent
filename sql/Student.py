from sql.SQLManager import SQLManager


class Student:
    def __init__(self, manager: SQLManager):
        self.manager = manager
        self.conn = manager.conn
        self.cursor = manager.cursor

    def create_student(self, name, age):
        self.cursor.execute("INSERT INTO students (name, age) VALUES (?, ?)", (name, age))
        self.conn.commit()
    
    def get_students(self):
        self.cursor.execute("SELECT * FROM students")
        self.conn.commit()
        return self.cursor.fetchall()
    
    def get_student(self, student_id):
        self.cursor.execute("SELECT * FROM students WHERE student_id=?", (student_id,))
        self.conn.commit()
        return self.cursor.fetchone()

    def update_student(self, student_id, name, age):
        self.cursor.execute("UPDATE students SET name=?, age=? where student_id=?", (name, age, student_id))
        self.conn.commit()

    def delete_student(self, student_id):
        self.cursor.execute("DELETE FROM students WHERE student_id=?", (student_id,))
        self.conn.commit()

if __name__ == "__main__":
    db = SQLManager()
    student = Student(db)
    student.create_student('Ibrahim', 30)
    student.create_student('Ali', 31)
    student.create_student('Sarah', 22)
    student.create_student('Ahmed', 27)
    student.create_student('Samer', 37)
    res = student.get_students()