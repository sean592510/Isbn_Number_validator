# web_app.py
from flask import Flask, request, render_template_string
from isbn_validator import validate_isbn

app = Flask(__name__)

HTML = '''
<!DOCTYPE html>
<html>
<head>
    <title>ISBN Validator</title>
    <style>
        body { font-family: Arial; margin: 50px; background: #f4f4f4; }
        .container { max-width: 600px; margin: auto; padding: 30px; background: white; border-radius: 10px; box-shadow: 0 0 10px rgba(0,0,0,0.1); }
        input, button { padding: 10px; font-size: 16px; margin: 10px 0; width: 100%; }
        button { background: #007bff; color: white; border: none; cursor: pointer; }
        button:hover { background: #0056b3; }
        .result { margin-top: 20px; padding: 15px; border-radius: 5px; font-weight: bold; }
        .valid { background: #d4edda; color: #155724; }
        .invalid { background: #f8d7da; color: #721c24; }
    </style>
</head>
<body>
<div class="container">
    <h1>ISBN Validator</h1>
    <p>Enter ISBN-10 or ISBN-13 (with or without hyphens)</p>
    <form method="post">
        <input type="text" name="isbn" placeholder="e.g. 978-0261103573 or 0306406152" required>
        <button type="submit">Validate</button>
    </form>
    {% if result %}
    <div class="result {{ 'valid' if result.valid else 'invalid' }}">
        {{ result.message }}
    </div>
    {% endif %}
</div>
</body>
</html>
'''

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        isbn = request.form["isbn"]
        valid = validate_isbn(isbn)
        result = {
            "valid": valid,
            "message": f"Valid ISBN: {isbn}" if valid else f"Invalid ISBN: {isbn}"
        }
    return render_template_string(HTML, result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
