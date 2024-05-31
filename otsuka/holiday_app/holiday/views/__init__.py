#ここはビューファイルです。

#flask関連の必要なパッケージをインポート
from flask import request, redirect, url_for, render_template, flash, session

#__init__.pydeで作成したappをインポート
from holiday import app

#URLにアクセスがあった時の処理
#http:127.0.0.1.5000/にリクエストがあった時
@app.route('/')
#show_entries()というメソッドが呼ばれる
def show_entries():
    #templatesフォルダ以下にあるentries/index.htmlを返す設定
    return render_template('input.html')

#/loginというURLにリクエストがあった時のルーティング処理
@app.route('/login', methods=['GET', 'POST'])
def login():
    #祝日日付フォームに入力されたデータが送られたときの処理
    if request.method == 'POST':
        if request.form['holiday'] != app.config['HOLIDAY']:
            print('ホリデイ入力したね')
        elif request.form['holiday_text'] != app.config['HOLIDAY_TEXT']:
            print('テキスト入力したね～')
        else:
            return redirect('/')
        #間違っている時は再度入力フォームを表示させる
        return render_template('input.html')

#ログアウトされたときの処理
@app.route('/logout')
def logout():
    #ホーム画面にも同様にする
    return redirect('/')