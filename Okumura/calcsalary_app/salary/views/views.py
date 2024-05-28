from flask import request, redirect, url_for, render_template, flash, session
from salary import app

# Readme: / にリクエストがあった時の処理
@app.route("/")
def input():
    return render_template('input.html')