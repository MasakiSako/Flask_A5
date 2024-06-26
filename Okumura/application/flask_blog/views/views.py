from flask import request, redirect, url_for, render_template, flash, session
from flask_blog import app
from functools import wraps

# Create: Decolator
def login_required(view):
    @wraps(view)
    def inner(*args, **kwargs):
        if not session.get('logged_in'):
            return redirect(url_for('login'))
        return view(*args, **kwargs)
    return inner

# Readme: / にリクエストがあった時の処理
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            flash('ユーザ名が異なります')
        elif request.form['password'] != app.config['PASSWORD']:
            flash('パスワードが異なります')
        else:
            session['logged_in'] = True
            flash("ログインしました？")
            return redirect(url_for('show_entries'))
    return render_template('login.html')


@app.route('/logout')
def logout():
    # Readme: ログアウトでセッション情報を削除
    session.pop('logged_in', None)
    flash('ログアウトした？')
    return redirect(url_for('show_entries'))
