from flask import request, redirect, url_for, render_template, flash, session
from salary import app

# Readme: / にリクエストがあった時の処理
@app.route('/')
def lp():
    return redirect(url_for('input'))

@app.route('/input')
def input():
    return render_template('input.html')

@app.route('/output')
def output():
    return render_template('output.html')