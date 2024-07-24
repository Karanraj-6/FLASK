from flask import Flask,redirect,url_for,render_template
from form import signupform,loginform
app = Flask(__name__)
app.config["SECRET_KEY"]="this_is_a_secret_key"

@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html",title="home")

@app.route('/signup')
def singup():
    form=signupform()
    if form.validate_on_submit():
        return redirect(url_for('/home'))
        
    return render_template("signup.html",title="singup",form=form)

@app.route('/login')
def login():
    form=loginform()
    return render_template("login.html",title="login",form=form)

if __name__ == "__main__":
    app.run(debug=True)