from flask import request, redirect, url_for, render_template, flash, session
from attendance import app ,db
from attendance.models.entries import Entry , NameList

@app.route('/masterresult', methods=['POST'])
def custom_namels():
    dupcheck = NameList.query.filter_by(name= request.form['offname']).first()
    if request.form['offname']=="" or request.form['offpass']=="":
        rsltmsg = "正しく入力してください"
        flash(rsltmsg)
        return redirect(url_for('master_view'))
    if request.form["button"] == 'insert':
        if dupcheck is not None:
            rsltmsg = "その名前は登録済です"
            flash(rsltmsg)
            return redirect(url_for('master_view'))
        else:
            entry = NameList(
            name = request.form['offname'],
            logpass = request.form['offpass'],
            isMaster  = "N"
            )
            rsltmsg = request.form['offname'] + "が登録されました"
            db.session.add(entry)
            db.session.commit()
        return render_template('masterresult.html',msg = rsltmsg)
    elif request.form["button"] == 'delete':
        if dupcheck is not None:
            entry = NameList.query.get(request.form['offname'])
            db.session.delete(entry)
            db.session.commit()           
            rsltmsg = request.form['offname'] + "は、削除されました"
            return render_template('masterresult.html',msg = rsltmsg)
        else:
            rsltmsg = request.form['offname'] + "は、マスタに登録されていません"
            flash(rsltmsg)
            session["input_data"] = request.form['offname']
            return redirect(url_for('master_view'))
        