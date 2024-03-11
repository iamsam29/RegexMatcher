from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/results", methods=["POST"])
def results():
    test_string = request.form.get("test_string")
    regex_pattern = request.form.get("regex_pattern")
    matched_strings = re.findall(regex_pattern, test_string)
    return render_template("results.html", matched_strings=matched_strings)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
