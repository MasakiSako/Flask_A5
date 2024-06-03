from flask import request, redirect, url_for, render_template, flash, session
from attendance import app ,db
from functools import wraps
from attendance.models.entries import Entry , NameList
import datetime
from sqlalchemy import and_

def login_required(view):
    @wraps(view)
    def inner(*args, **kwargs):
        if not session.get("logged_in"):
            return redirect(url_for('login'))
        return view(*args, **kwargs)
    return inner

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        if request.form['username']=="":
            rsltmsg = "名前を入力してください"
            flash(rsltmsg)
            return redirect('/')
        dupcheck = NameList.query.filter_by(name= request.form['username']).first()
        if dupcheck is None:
            rsltmsg = "登録された名前を入力してください"
            flash(rsltmsg)
            return redirect('/')
        entry = NameList.query.get(request.form['username'])
        if request.form['password'] != entry.logpass:
            flash("パスワードが異なります")
            return redirect('/')
        else:
            if entry.isMaster == 'Y':
                session['logged_in'] = True
                flash('ログインしました')
                return redirect('/master')
            else:
                dated = datetime.datetime.today()
                dupcheck2 = db.session.query(Entry).filter(and_(Entry.name == request.form['username'],Entry.date==dated)).all()
                if dupcheck2 is None:
                    oentry = Entry(
                    name = request.form['username'],
                    date = dated
                    )
                    db.session.add(oentry)
                    db.session.commit()
                    return redirect('/result')
                else: 
                    flash('既に出席済みです')
                    return redirect('/login')
    return render_template('login.html')

@app.route('/result')
def showresult():
    session.pop('logged_in',None)
    return render_template('result.html')

@app.route('/logout')
def logout():
    session.pop('logged_in',None)
    flash('ログアウトしました')
    return redirect('/')

@app.route('/master')
@login_required
def master_view():
    init_val = session.get("input_data", None)
    session.pop('input_data',None)
    return render_template('master.html',defdata = init_val)
    