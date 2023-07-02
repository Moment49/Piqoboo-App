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


user_info = {}
@app.route('/signUp', methods=['GET', 'POST'])
def signUp():
    name = None
    email = None
    password = None
    c_password = None
    form = RegisterForm() 
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data
        c_password = form.confirm_password.data
        if password == c_password:
            flash("Password match")
            # Push to the dictionary
            form.name.data = ''
            form.email.data = ''
            form.password.data = ''
            form.confirm_password.data = '' 
        else:
            flash("password does not match")
        
             
    return render_template('signUp.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if session.get('full_name'):    
        if form.validate_on_submit():
            email = form.email.data
            password = form.password.data
            if email in session['email'] and password in session['password']:
                print("found")
                return redirect(url_for('dashboard'))
            else:
                return redirect(url_for('signUp'))
        return render_template('login.html', form=form)
    else:
        return redirect(url_for('signUp'))


# dashboard route
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

   

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