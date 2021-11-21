# Author: Murtadha Marzouq
# Date: 2020-11-24
# Group: 15 
# Assignment: Final Project

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField,TextField
class ContactForm(FlaskForm):
    name = TextField("Name")
    email = TextField("Email")
    subject = TextField("Subject")
    message = TextAreaField("Message")
    submit = SubmitField("Send")

from flask_wtf import Form
from flask_wtf import FlaskForm
from flask_wtf import Form
#importing the necessary libraries (Death by a thousand cuts)
from flask import Flask, render_template, request
from wtforms import StringField, PasswordField, BooleanField, SubmitField
#from flaskext.wtf import Form, FileField, FieldList, required
from forms import LoginForm
from forms import RegisterForm
from flask_wtf import FlaskForm
import bcrypt
from flask import request
from flask import session
from models import User as User
from database import db
from flask import url_for
from flask import redirect
from flask import request
from flask import render_template
import os  # os is used to get environment variables IP & PORT
from flask import Flask, render_template

app = Flask(__name__) 
# Setting up the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Travel_app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'GROUPROJECT'
app.config["IMAGE_UPLOADS"] = "static"
# Initializing the database (Death by a thousand cuts)
db.init_app(app)
with app.app_context():
    db.create_all()  
    
@app.route('/contact', methods=['POST', 'GET'])
def contact():
    contact = ContactForm()
    if request.method == 'POST':
        return 'Thank you'
    return render_template("contact.html", form=contact)
# TESTING

@app.route('/test')
def test():
    return render_template("test.html")



# Setting up the routes
@app.route('/')
def home():
    return render_template("Home.html")


# Setting up the routes
@app.route('/parners')
def partners():
    return render_template("partners.html")

@app.route('/login', methods=['POST', 'GET'])
def login():
    login_form = LoginForm()
    # Checking if the user is already logged in
    if login_form.validate_on_submit():
        the_user = db.session.query(User).filter_by(
            email=request.form['email']).one()
        # Checking if the password is correct
        saltp = bcrypt.gensalt(14)
        hashp = bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.gensalt(14)) 
        
        # if bcrypt.checkpw(request.form['password'].encode('utf-8'), the_user.password):
        if bcrypt.checkpw(request.form['password'].encode('utf-8'), the_user.password.encode('utf-8')):
            session['user'] = the_user.first_name
            session['user_id'] = the_user.id
            return redirect(url_for('index'))
        # If the password is incorrect
        login_form.password.errors = ["Incorrect username or password."]
        return render_template("login.html", form=login_form)
    else:
        # If the user is not logged in
        return render_template("login.html", form=login_form)

# Loging out user
@app.route('/logout')
def logout():
    if session.get('user'):
        session.clear()

    return redirect(url_for('login'))


# REGISTRATION PAGE #
@app.route('/register', methods=['POST', 'GET'])
def register():
    form = RegisterForm()

    if request.method == 'POST' or request.method == 'GET' and form.validate_on_submit():
        # salt and hash password
        h_password = bcrypt.hashpw(
            request.form['password'].encode('utf-8'), bcrypt.gensalt(14))
        # get entered user data
        first_name = request.form['firstname']
        last_name = request.form['lastname']
        # create user model
        new_user = User(first_name, last_name,
                        request.form['email'], h_password)
        db.session.add(new_user)
        db.session.commit()
        session['user'] = first_name
        session['user_id'] = new_user.id
        return redirect(url_for('index'))

    return render_template('register.html', form=form)

# routing to the index page
@app.route('/index')
def index():
    if session.get('user'):
        return render_template("index.html", user=session['user'])
    else:
        return redirect(url_for('login'))

# routing user profile page (not yet completely implemented)
@app.route('/profile/userID')
def profile():
    # insert code
    if session.get('user'):
        user = db.session.query(User).filter_by(id=session['user_id']).one()
        return render_template("profile.html", user=user)
    else:
        return redirect(url_for('login'))
