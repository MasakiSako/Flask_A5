from flask import request, redirect, url_for, render_template, flash, session

def calc_salary(salary):
     # 給与計算
     if salary > 1000000:
          tax = round((salary - 1000000) * 0.2) + round(1000000 * 0.1)
          paid = salary - tax
     else:
          tax = round(salary * 0.1)
          paid = round(salary - tax)
             
     result = "給与：" + str("{:,}".format(salary)) + "の場合、支給額：" + str("{:,}".format(paid)) + "円、税額：" + str("{:,}".format(tax)) + "円です。"
     print(result)
     return result