#!/usr/bin/env python3
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("hellobasic.html")

# pull in the value of score as an int
@app.route("/scoretest/<int:score>")
def hello_name(score):
    # render the template with the value of score for marks
    # marks is a jinja var in the template
    return render_template("highscore.html", marks = score)

#grab the value 'username'
@app.route("/<username>")
def login(username):
    # render the jinja template "helloname.html"
    # apply the value of username for the var name
    return render_template("helloname.html", name = username)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224, debug=True)

