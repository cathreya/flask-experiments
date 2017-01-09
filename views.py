from flask import render_template, flash, redirect
from .forms import LoginForm
from app import app


@app.route('/')
def index():
	return("<h1>HELLO WORLD</h1>")
 
@app.route('/login')
def login():
	form1 = LoginForm()
	return render_template('login.html', title='Sign In', form=form1)