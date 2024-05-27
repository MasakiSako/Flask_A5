#ビューファイルの作成
#http://127.0.0.1:5000/にリクエストがあったときの処理を書く

#__init__.pyで作成したappをインポート
#from flask_blog import app

#flask関連の必要なパッケージをimport
from flask import request, redirect, url_for, render_template, flash, session
from flask_blog import app

#@app.route('/')
#def show_entries():
#    return "Hello World!"

#templatesフォルダ以下にあるentries/index.htmlを返してあげる
@app.route('/')
def show_entries():
    return render_template('entries/index.html')

#16章ビューを追加する
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            print('ユーザー名が異なります')
        elif request.form['password'] !=app.config['PASSWORD']:
            print('パスワードが異なります')
        else:
            return redirect('/')
        return render_template('login.html')

@app.route('/logout')
def logout():
    return redirect('/')
