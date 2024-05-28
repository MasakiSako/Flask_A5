from flask import request, redirect, url_for, render_template, flash, session
from salary import app
import math
@app.route('/')
def home():
    init_val = session.get("input_data", None)
    return render_template('input.html',defdata = init_val)
@app.route('/output',methods=['GET','POST'])
def calc():
    if request.method == 'POST':
        # 入力フォームが空か
        if request.form['salary'] == "":
            flash("給料が未入力です。入力してください")
        elif int(request.form['salary']) >=1e10:
            flash("給料には最大9,999,999,999まで入力可能です。")
            session["input_data"] = request.form['salary']
        elif int(request.form['salary']) <0:
            flash("給料にはマイナスの値は入力できません。")
            session["input_data"] = request.form['salary']
        else:
            flash('計算しました')
            sal = int(request.form['salary'])
            input_salary=[sal,0,0]
            if sal > 1e6:
                input_salary[2] = math.floor(0.2*sal - 1e5)
                input_salary[1] = sal - input_salary[2]
            else :
                input_salary[2] = math.floor(0.1*sal)
                input_salary[1] = sal - input_salary[2]
            return render_template("output.html",salary=input_salary)
    return redirect('/')


