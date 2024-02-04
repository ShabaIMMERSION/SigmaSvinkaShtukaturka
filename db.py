from sqlmanager import SQLManager

sql = SQLManager("quizz.db")
sql.create_tables()

sql.add_quizz("SigmaSvinka", "Quizz about Sanya Forgottentimsov")