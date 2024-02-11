from sqlmanager import SQLManager

sql = SQLManager("quizz.db")
sql.create_tables()

sql.add_quizz("SigmaSvinka", "Quizz about Sanya Forgottentimsov")
sql.add_question(1, "Sigma Svinka?")
sql.add_answers(1, "No, I am not. I'm Sigma Shtukaturka", True)

