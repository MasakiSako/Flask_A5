from flask import request, redirect, url_for, render_template, flash, session
from salary import app
from decimal import Decimal, ROUND_HALF_UP

@app.route('/', methods=['GET', 'POST'])
def input():
   
    return render_template("input.html")

@app.route('/output', methods=['GET', 'POST'])
def output():
    salary = int(request.form['salary'])
    if salary >= 1000000:
        tax = (salary - 1000000)*0.2 + 100000
        tax = Decimal(str(tax)).quantize(Decimal("0"), rounding= ROUND_HALF_UP)
        sikyu = salary - tax
    elif salary < 0:
        flash('給与にはマイナスの値は入力できません')
    else:
        tax = salary * 0.1
        tax = Decimal(str(tax)).quantize(Decimal("0"), rounding= ROUND_HALF_UP)
        sikyu = salary - tax
      
    return render_template("output.html", input_salary = salary, input_sikyu = sikyu, input_tax = tax)


# @app.route('/logout')
# def logout():
#     session.pop('logged_in', None)
#     flash('ログアウトしました')
#     return redirect(url_for('show_entries'))


# import sys
# arg = sys.argv

# from decimal import Decimal, ROUND_HALF_UP

# salary = int(arg[1])

# tax = (salary - 1000000)*0.2 + 100000



# if salary >= 1000000:
#     tax = (salary - 1000000)*0.2 + 100000
#     tax = Decimal(str(tax)).quantize(Decimal("0"), rounding= ROUND_HALF_UP)
#     sikyu = salary - tax
#     print(f"支給額:{sikyu}、", end="")
#     print(f"税額:{tax}", end="")
# else:
#     tax = salary * 0.1
#     tax = Decimal(str(tax)).quantize(Decimal("0"), rounding= ROUND_HALF_UP)
#     sikyu = salary - tax
#     print(f"支給額:{sikyu}、", end="")
#     print(f"税額:{tax}", end="")