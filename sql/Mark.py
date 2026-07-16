from sql.SQLManager import SQLManager
class StudentSubject:
  def __init__(self, manager: SQLManager):
    self.manager = manager
    self.cursor = manager.cursor
    self.conn = manager.conn

  def add_mark(self, student_id, subject_id, mark):
    self.cursor.execute("INSERT INTO student_marks (student_id, subject_id, mark) VALUES (?,?,?)", (student_id, subject_id, mark))
    self.conn.commit()

  def get_marks(self):
    self.cursor.execute("SELECT * FROM student_marks")
    self.conn.commit()
    return self.cursor.fetchall()
  
if __name__ == "__main__":
    db = SQLManager()
    student_subject = StudentSubject(db)
    student_subject.add_mark(1, 1, 90)
    student_subject.add_mark(1, 2, 80)
    student_subject.add_mark(2, 1, 70)
    student_subject.add_mark(2, 2, 60)
    student_subject.add_mark(3, 1, 50)
    student_subject.add_mark(3, 2, 40)
    student_subject.add_mark(4, 1, 30)
    student_subject.add_mark(4, 2, 20)
    student_subject.add_mark(5, 1, 10)
    student_subject.add_mark(5, 2, 0)