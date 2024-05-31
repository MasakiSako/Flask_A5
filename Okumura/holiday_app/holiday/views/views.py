from flask import request, redirect, url_for, render_template, flash, session
from holiday import app

@app.route('/')
def show_home():
    return render_template('entries/input.html')
