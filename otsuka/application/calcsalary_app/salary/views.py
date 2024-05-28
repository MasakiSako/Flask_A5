from flask import request, redirect, url_for, render_template, flash, session
from salary import app
from decimal import Decimal, ROUND_HALF_UP

@app.route('/')
def show_templates():
   # if not session.get('logged_in'):
    #    return redirect(url_for('login'))
    return render_template('input.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        
        kyuuyogaku = int(request.form['salary'])
        

      #  elif request.form['password'] !=app.config['PASSWORD']:
       # if kyuuyogaku == '':
       #     flash('給与が未入力です。入力してください。')
        
        if kyuuyogaku > 9999999999:
            flash('給与には最大9,999,999,999まで入力可能です。')
        
        elif kyuuyogaku < 0:
            flash('給与にはマイナスの値は入力できません。')

        elif kyuuyogaku > 1000000:
            zeigaku = int((kyuuyogaku-1000000) * 0.2 + 100000)
            sikyuugaku = kyuuyogaku - zeigaku
        elif:
            zeigaku = int(kyuuyogaku*0.1)
            sikyuugaku = kyuuyogaku - zeigaku
        
        else :
            flash('給与が未入力です。入力してください。')
        syuturyoku = "給与:"+str(kyuuyogaku)+"の場合、支給額："+str(sikyuugaku)+"円、税額："+str(zeigaku)+"円です。" 
        # if request.form['username'] != app.config['USERNAME']:
        #     flash('ユーザー名が異なります')
        # elif request.form['password'] !=app.config['PASSWORD']:
        #     flash('パスワードが異なります')
        # else:
        #     session['logged_in'] = True
        #     flash('ログインしました')
        #     return redirect(url_for('show_templates'))
    return render_template("output.html", salary = syuturyoku)

@app.route('/logout')
def logout():
    session.pop('logged_in',None)
    flash('ログアウトしました')
    return redirect(url_for('show_temolates'))