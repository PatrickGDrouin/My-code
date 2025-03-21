#!/usr/bin/python3

from flask import Flask
from flask import redirect
from flask import url_for
from flask import request

app = Flask(__name__)

### NOTE FROM CHAD: There is nothing wrong with the HTML
html= '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Trivia Time</title>
    <style>
        body {
            background-color: black;
            text-align: center;
            color: white;
            font-family: Arial, Helvetica, sans-serif;
        }
    </style>
</head>
<body>

    <h1>TRIVIA TIME</h1>
    <p>What is the meaning of life, the universe, and everything?</p>
    <img src="https://stevetobak.com/wp-content/uploads/2021/02/dont-panic.png" alt="Avatar" style="width:200px">

    <form action="/login" method="POST">
        <p><input type = "text" name = "nm"></p>
        <p><input type = "submit" value = "submit"></p>
    </form>

</body>
</html>'''
@app.route("/success")
def success():
    return f"That is correct!"

@app.route("/")
def start():
    return html

@app.route("/login", methods = ["POST"])
def login():
    # if request.form.get["nm"] == "42": # oh my bad!!! you had asked if this was ok and I said yes... there's a small syntax error here
    if request.form.get("nm") == "42": # .get() is a method, so use () instead of []. Sorry!
        # return redirect(url_for("/success"))
        return redirect(url_for("success"))
    else:
        # return redirect(url_for("/"))
        return redirect(url_for("start")) # be careful- when using url_for(), you have to pass the name of the function (not the endpoint)

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224, debug=True)
