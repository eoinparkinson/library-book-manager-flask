from pathlib import Path
import requests
from flask import Flask, request, render_template

app = Flask(__name__)

# finding the path of books.txt
"""
dataFolder = Path(r'data/books.txt')
fileToOpen = dataFolder / "books.txt"
"""


# opening data/books.txt
f = open("books.txt","r")

print(f.read())

# Homepage
@app.route("/", methods=["GET","POST"])
def searchBookForm():
    if request.method == "POST":
        if request.form["submitButton"] == "Search":
            text = request.form["book-name"]
            processed_text = text.lower()
            return render_template("my-form.html", message="Returning search results for: "+processed_text)

        else:
            text = ""
            return render_template("my-form.html", message="")

    else:
        text = ""
        return render_template("my-form.html", message="")

# Add Book Page
@app.route("/add-book", methods=["GET","POST"])
def addBookForm():
    return render_template("add-book.html")


if __name__ == "__main__":
    app.run(debug=True)
