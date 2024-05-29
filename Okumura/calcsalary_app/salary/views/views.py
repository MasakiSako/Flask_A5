from flask import request, redirect, url_for, render_template, flash, session
from salary import app
from .module import calc_salary

# Readme: / にリクエストがあった時の処理
@app.route('/')
def main():
    init_val = session.get('input_data', None)
    session.pop('input_data', None)
    return render_template('input.html', defdata = init_val)

@app.route('/input')
def input():
    return render_template('input.html')

@app.route('/output', methods=['GET', 'POST'])
def output():
    salary = request.form['salary']

    try:
        salary = int(salary)
    except:
        flash("整数で入力してください")
        return render_template('input.html')

    if salary == "":
        flash("給与が未入力です。入力してください。")
    elif salary > 10:
        flash("給与には最大9,999,999,999まで入力可能です。")
    elif salary < 0:
        flash("給与にはマイナスの値は入力できません。")
    else:
        result = calc_salary(salary)
        return render_template('output.html', result=result)
    
    session["input_data"] = salary
    return redirect('/')