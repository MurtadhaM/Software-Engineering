# Author: Murtadha Marzouq
# Date: 2020-11-24
# Group: 15 
# Assignment: Final Project

import flask
#importing the necessary libraries (Death by a thousand cuts)
from forms import LoginForm
from forms import RegisterForm
import bcrypt
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
    

# TESTING
@app.route('/')
@app.route('/barchart')
def barchart():
    return render_template("Home.html", value="barchart.html")


@app.route('/stacked')
def stacked():
    return render_template("Home.html", value="stacked.html")

@app.route('/line')
def line():
    return render_template("Home.html", value="line.html")

@app.route('/multi')
def multi():
    return render_template("Home.html", value="multi.html")

@app.route('/bubble')
def bubble():
    return render_template("Home.html", value="bubble.html")
@app.route('/heatmap')
def heatmap():
    return render_template("Home.html", value="heatmap.html")


