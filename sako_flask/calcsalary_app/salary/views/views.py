from flask import request, redirect, url_for, render_template, flash, session
from salary import app
import math
@app.route('/')

@app.route('/input',methods=['GET','POST'])
def calc():
    if request.method == 'POST':
        if request.form['salary'] == "":
            flash("給料を入力してください")
        else:
            flash('計算します')
            sal = request.form['salary']
            input_salary=[sal,0,0]
            if sal > 1e6:
                input_salary[2] = math.floor(0.2*sal - 1e5)
                input_salary[1] = sal - input_salary[2]
            else :
                input_salary[2] = math.floor(0.1*sal)
                input_salary[1] = sal - input_salary[2]
            return render_template('output.html',salary=input_salary)
    return redirect(url_for('calc'))

# @app.route('/logout')
# def logout():
#     session.pop('logged_in',None)
#     flash('ログアウトしました')
#     return redirect(url_for('show_entries'))