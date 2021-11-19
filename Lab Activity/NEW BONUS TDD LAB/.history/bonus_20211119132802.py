# Author: Murtadha Marzouq
# Date: 2020-11-24
# Group: 15 
# Assignment: Final Project

import flask
#importing the necessary libraries (Death by a thousand cuts)
from flask import url_for
from flask import redirect
from flask import request
from flask import render_template
import os  
from flask import Flask, render_template

app = Flask(__name__) 
# Setting up the database
    

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


