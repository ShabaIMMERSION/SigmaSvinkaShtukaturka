import sqlite3

class SQLManager:
    def __init__(self, db_name):
        self.db = sqlite3.connect(db_name)

    def create_tables(self):
        cursor = self.db.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Quizz (
            quizz_id INTEGER PRIMARY KEY,
            quizz_name TEXT NOT NULL,
            description TEXT
            )
        ''')
        cursor.execute('''
                      CREATE TABLE IF NOT EXISTS Questions (
                           question_id INTEGER PRIMARY KEY,
                           quiz_id INTEGER,
                           content TEXT,
                           FOREIGN KEY (quiz_id) REFERENCES Quizz(quiz_id)
                      );
                      ''')
        cursor.execute('''
                      CREATE TABLE IF NOT EXISTS Answers (
                           answer_id INTEGER PRIMARY KEY,
                           question_id INTEGER,
                           content TEXT,
                           is_right BOOLEAN,
                           FOREIGN KEY (question_id) REFERENCES Questions(question_id)
                      );
                      ''')
        cursor.close()
        self.db.commit()

    def add_quizz(self, name, description):
        cursor = self.db.cursor()
        cursor.execute("""
            INSERT INTO Quizz (quizz_name, description) VALUES (?, ?)
        """, [name, description])
        cursor.close()
        self.db.commit()
