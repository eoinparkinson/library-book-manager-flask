import base64
import requests
from flask import Flask, request, render_template

app = Flask(__name__)

#Basic image url to base64 (working)
@app.route("/")
def my_form():
    return render_template("my-form.html")

@app.route("/", methods=["POST"])
def my_form_post():
    text = request.form["book-name"]
    processed_text = text.lower()
    return render_template("my-form.html", message=processed_text)


if __name__ == "__main__":
    app.run(debug=True)
