from sql.SQLManager import SQLManager

class Subject:
    def __init__(self, manager: SQLManager):
        self.manager = manager
        self.conn = manager.conn
        self.cursor = manager.cursor

    def create_subject(self, subject_name):
        self.cursor.execute("INSERT INTO subjects (subject_name) VALUES (?)", (subject_name,))
        self.conn.commit()
    
    def get_subjects(self):
        self.cursor.execute("SELECT * FROM subjects")
        self.conn.commit()
        return self.cursor.fetchall()
    
   
if __name__ == "__main__":
    db = SQLManager()
    subject = Subject(db)
    subject.create_subject('Math')
    subject.create_subject('English')
    subject.create_subject('Science')
    subject.create_subject('History')
    subject.create_subject('Geography')
    subject.create_subject('Art')
    subject.create_subject('Music')
    subject.create_subject('Physical Education')
    subject.get_subjects()
