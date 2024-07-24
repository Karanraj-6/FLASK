from flask_wtf import FlaskForm
from wtforms import StringField,SelectField,DateField,PasswordField,SubmitField,BooleanField
from wtforms.validators import DataRequired,Length,Email,Optional,EqualTo

class signupform(FlaskForm):
    username=StringField("username",validators=[DataRequired(),Length(2,30)])
    email=StringField("email",validators=[DataRequired(),Email()])
    gender=SelectField("gender",choices=["male","female","other"],validators=[Optional()])
    DateOfBirth=DateField("DateOfBirth",validators=[Optional()])
    password=PasswordField("password",validators=[DataRequired(),Length(5,20)])
    ConfirmPassword=PasswordField("ConfirmPassword",validators=[DataRequired(),Length(5,20),EqualTo('password')] )
    submit=SubmitField("Signup")
                          

class loginform(FlaskForm):
    email=StringField("email",validators=[DataRequired(),Email()])
    password=PasswordField("password",validators=[DataRequired(),Length(5,20)])
    remember=BooleanField("Remember Me")
    submit=SubmitField("Login")
    

