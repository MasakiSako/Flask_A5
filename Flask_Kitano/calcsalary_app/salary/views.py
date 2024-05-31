from flask import request, redirect, url_for, render_template, flash, session
from salary import app
from decimal import Decimal, ROUND_HALF_UP

@app.route('/', methods=['GET', 'POST'])
def input():
    input_salary = session.get("input_data", None)
    return render_template("input.html")

@app.route('/output', methods=['GET', 'POST'])
def output():
    salary = request.form['salary']
    if len(salary) >= 10:
        flash('給与には最大9,999,999,999まで入力可能です。')
        return redirect(url_for('input'))
    elif salary == "":
        flash('給与が未入力です。入力してください。')
        return redirect(url_for('input'))
    
    salary = int(request.form['salary'])
    if salary < 0:
        flash('給与にはマイナスの値は入力できません')
        return redirect(url_for('input'))
    elif salary >= 1000000:
        tax = (salary - 1000000)*0.2 + 100000
        tax = Decimal(str(tax)).quantize(Decimal("0"), rounding= ROUND_HALF_UP)
        sikyu = salary - tax

    # elif salary == "":
    #     flash('給与が未入力です。入力してください。')
    #     return redirect(url_for('input'))
    else:
        tax = salary * 0.1
        tax = Decimal(str(tax)).quantize(Decimal("0"), rounding= ROUND_HALF_UP)
        sikyu = salary - tax
      
    return render_template(
        "output.html", 
        input_salary = salary, 
        input_sikyu = sikyu, 
        input_tax = tax)
    return redirect(url_for('input'))
