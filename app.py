# import sqlite3
import requests
from flask import Flask, request, render_template

app = Flask(__name__)

"""
DB_PATH = './books_database.db'   # Update this path accordingly
NOTSTARTED = 'Not Started'
INPROGRESS = 'In Progress'
COMPLETED = 'Completed'
"""

"""
#Calling home directory
@app.route("/")
def my_form():
    return render_template("my-form.html")
"""

@app.route("/")
def my_form_post():
    if request.method == "POST":
        if request.form["submitButton"] == "searchBook":
            text = request.form["book-name"]
            processed_text = text.lower()
            return render_template("my-form.html", message=processed_text)

        elif request.form["submitButton"] == "addBook":
            return render_template("add-book.html")

        else:
            return render_template("my-form.html", message="")

    else:
        return render_template("my-form.html", message="")


if __name__ == "__main__":
    app.run(debug=True)
