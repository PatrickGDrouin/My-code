from flask import Flask
from flask import redirect
from flask import url_for

app= Flask(__name__)

@app.route("/admin") # website main call
def hello_admin():
    return f"hello admin!"

@app.route("/guest/<guesty>")
def hello_guest(guesty):
    return f"hello {guesty} guest"

@app.route("/user/<name>")
def hello_user(name):
    if name == "admin":
        return redirect(url_for("hello_admin"))
    else:
        return redirect(url_for("hello_guest", guesty = name))

if __name__ == "__main__":
    app.run(port=2224,host="0.0.0.0")
