from flask import Flask, render_template
from sqlmanager import SQLManager


app = Flask(__name__)


@app.route('/')
def index():
    return render_template("main.html")


@app.route('/quizzes')
def quizzes():
    sql = SQLManager("quizz.db")
    quizzes = sql.select_quizzes()
    return render_template("quizzes.html", quizzes=quizzes)



if __name__ == "__main__":
    app.run()
