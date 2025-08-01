from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = "super_secret_key"  # For session security

# Sample Questions
QUESTIONS = [
    {
        "question": "Who is the creator of Python?",
        "options": ["Guido van Rossum", "Elon Musk", "Mark Zuckerberg", "Bill Gates"],
        "correct": "Guido van Rossum"
    },
    {
        "question": "Which language is Flask written in?",
        "options": ["Java", "Python", "C++", "Ruby"],
        "correct": "Python"
    },
    {
        "question": "Which brackets are used to create a list in Python?",
        "options": ["()", "[]", "{}", "<>"],
        "correct": "[]"
    },
    {
        "question": "Which brackets are used to create a dictionary in Python?",
        "options": ["()", "[]", "{}", "<>"],
        "correct": "{}"
    },
    {
        "question": "What is the alternative of 'and' in Python?",
        "options": ["&", "&&", "+", "||"],
        "correct": "&"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["function", "def", "func", "define"],
        "correct": "def"
    },
    {
        "question": "Which keyword is used to define a class in Python?",
        "options": ["class", "struct", "object", "type"],
        "correct": "class"
    },
    {
        "question": "Which function is used to get the type of a variable in Python?",
        "options": ["typeof()", "type()", "instanceof()", "what_is()"],
        "correct": "type()"
    },
    {
        "question": "Which method is used to sort a list in Python?",
        "options": ["order()", "sort()", "arrange()", "organize()"],
        "correct": "sort()"
    },
    {
        "question": "Which mode is used to read a file in Python?",
        "options": ["r", "w", "a", "x"],
        "correct": "r"
    }
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/start")
def start_quiz():
    session["question_index"] = 0
    session["score"] = 0
    return redirect(url_for("show_question"))

@app.route("/question")
def show_question():
    index = session.get("question_index", 0)
    if index >= len(QUESTIONS):
        return redirect(url_for("result"))
    question = QUESTIONS[index]
    return render_template("quiz.html", question=question, index=index)

@app.route("/answer", methods=["POST"])
def handle_answer():
    user_answer = request.form.get("answer")
    index = session.get("question_index", 0)
    if user_answer == QUESTIONS[index]["correct"]:
        session["score"] += 10
    session["question_index"] = index + 1
    return redirect(url_for("show_question"))

@app.route("/result")
def result():
    score = session.get("score", 0)
    return render_template("result.html", score=score, total=len(QUESTIONS)*10)

if __name__ == "__main__":
    app.run(debug=True)
