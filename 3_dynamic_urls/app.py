from flask import Flask,render_template,url_for
from employee_data  import employees_data

app= Flask(__name__)

@app.route('/')
@app.route("/home")
def home():
    return render_template("home.html",title="home")

@app.route("/about")
def about():
    return render_template("about.html",title="about")

@app.route('/evaluate/<int:num>')
def evaluate(num):
    return render_template("evaluate.html",title="Evaluate",number=num)

@app.route("/employee")
def employee():
    return render_template("employee.html",title="employee",emps=employees_data)
    
    
if __name__ == "__main__":
    app.run(debug='True')