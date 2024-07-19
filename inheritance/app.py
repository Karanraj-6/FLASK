from flask import Flask,redirect,url_for
import time

app = Flask(__name__)

@app.route('/')
@app.route("/home")
def home():
    return "this is home page"

@app.route("/passed/<sname>/<int:smarks>")
def passed(sname,smarks):
    return f"congrats {sname} !your passed with {smarks} marks"

@app.route("/failed/<sname>/<int:smarks>")
def failed(sname,smarks):
    return f"sorry {sname}! your failed with {smarks} marks"


@app.route("/home/<name>/<int:marks>")
def eval(name,marks):
    if (marks >= 30):
        time.sleep(1)
        return redirect(url_for('passed',sname=name,smarks=marks))
    else:
        time.sleep(1)
        return redirect(url_for('failed',sname=name,smarks=marks))


if __name__ == "__main__":
    app.run(debug=True)
