from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route("/home")
def home():
    return "this is home page"

@app.route('/about')
def about():
    return "<h3>this is about section</h3>"

@app.route("/home/<name>")
def welcome(name):
    return f"hi {name}! welcome to webpage"

@app.route("/addtion/<int:num>")
def addition(num):
    return f"the given number is {num} and addtion of 10 to the number is {num+10}" 

@app.route('/addtion/<int:num1>/<int:num2>')
def addtion2(num1, num2):
    return f" the addtion of {num1} and {num2} is {num1+num2}"


if __name__ == "__main__":
    app.run(debug=True)
