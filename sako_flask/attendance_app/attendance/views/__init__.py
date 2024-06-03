from flask import request, redirect, url_for, render_template, flash, session
from attendance import app

@app.route('/')
def home():
    return render_template('login.html')


