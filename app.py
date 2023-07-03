from flask import Flask, render_template, redirect, url_for, session, flash, request
from flask_script import Manager
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo
import json

# Initialize the app obj
app = Flask(__name__)
manager = Manager(app)
app.config['SECRET_KEY'] = 'HCYSGIYISUGISYUGSYUGYSYD73782732'


#Set the routes
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/signUp', methods=['GET', 'POST'])
def signUp():
    form = RegisterForm() 
    password = None
    c_password = None
    if form.validate_on_submit():
        session['name'] = form.name.data
        session['email'] = form.email.data
        password = form.password.data
        c_password = form.confirm_password.data
        if password == c_password:
            flash("Sign up successful")
            session['password'] = password
            session['confirm_password'] = c_password
            return redirect(url_for('login'))   
        else:
            flash("password does not match")
            return redirect(url_for('signUp'))
    return render_template('signup.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
   email = None
   password = None
   form = LoginForm()
   if form.validate_on_submit():
       email = form.email.data
       password = form.password.data
       any_email = session.get('email')
       any_password = session.get('password')
       if email == any_email and password == any_password:
           flash('Login Successful')
           print(session['email'])
           form.email.data = ''
           form.password.data = ''
           return redirect(url_for('dashboard'))
       elif email != email or password != any_password:
           flash('invalid email or password')
           return redirect(url_for('login'))

   return render_template('login.html', form=form)


# dashboard route
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', name=session.get('name'))

   

# Register Form class
class RegisterForm(FlaskForm):
    name = StringField("name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField("Confirm password", validators=[DataRequired()])
    submit = SubmitField("Create Account")

# Login form class
class LoginForm(FlaskForm):
    email = StringField("Enter Email", validators=[DataRequired(), Email()])
    password = PasswordField("Enter password", validators=[DataRequired()])
    submit = SubmitField("Login")


class Logout(FlaskForm):
    submit = SubmitField("Logout")

if __name__ == '__main__':
    # manager.run()
    app.run(debug=True)