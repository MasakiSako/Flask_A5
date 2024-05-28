from flask import request, redirect, url_for, render_template, flash, session
from salary import app
from .module import calc_salary

# Readme: / にリクエストがあった時の処理
@app.route('/')
def lp():
    return render_template('input.html')

@app.route('/input')
def input():
    return render_template('input.html')

@app.route('/output', methods=['GET', 'POST'])
def output():
    # # 給与計算
    # if salary > 1000000:
    #      tax = round((salary - 1000000) * 0.2) + round(1000000 * 0.1)
    #      paid = salary - tax
    # else:
    #      tax = round(salary * 0.1)
    #      paid = round(salary - tax)
            
    # result = "給与：" + str("{:,}".format(salary)) + "の場合、支給額：" + str("{:,}".format(paid)) + "円、税額：" + str("{:,}".format(tax)) + "円です。"

    # return render_template('output.html', result=result)
    salary = request.form['salary']
    
    # 途中：インプット前に実装しないといけない
    if salary == "":
        flash("給与が未入力です。入力してください。")
    elif len(salary) > 10:
        flash("給与には最大9,999,999,999まで入力可能です。")
    elif salary < 0:
        flash("給与にはマイナスの値は入力できません。")
    else:
        result = calc_salary(int(salary))
        return render_template('output.html', result=result)