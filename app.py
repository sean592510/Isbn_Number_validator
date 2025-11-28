# app.py
from flask import Flask, render_template, request
from validator import validate_isbn_input

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    message = None
    valid = False

    if request.method == "POST":
        user_input = request.form["input"]
        valid, message = validate_isbn_input(user_input)

    return render_template("index.html", message=message, valid=valid)

if __name__ == "__main__":
    app.run(debug=True)
