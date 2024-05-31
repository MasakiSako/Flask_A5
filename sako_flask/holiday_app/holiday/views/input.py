from flask import request, redirect, url_for, render_template, flash, session
from holiday import app ,db
from holiday.models.mst_holiday import Entry

@app.route('/maintenance_date', methods=['POST'])
def add_entry():
    dupcheck = Entry.query.filter_by(holi_date= request.form['holiday']).first()
    if request.form["button"] == 'insert_update':
        entry = Entry(
            holi_date = request.form['holiday'],
            holi_text= request.form['holiday_text']
            )
        if dupcheck is not None:
            rsltmsg = request.form['holiday'] + "は「" + request.form['holiday_text'] + "」に更新されました"
            db.session.merge(entry)    
        else:
            rsltmsg = request.form['holiday'] + "(" + request.form['holiday_text'] + ")が登録されました"
            db.session.add(entry)
        db.session.commit()
        return render_template('result.html',msg = rsltmsg)
    elif request.form["button"] == 'delete':
        if dupcheck is not None:
            entry = Entry.query.get(request.form['holiday'])
            db.session.delete(entry)
            db.session.commit()           
            rsltmsg = request.form['holiday'] + "(" + entry.holi_text + ")は、削除されました"
            return render_template('result.html',msg = rsltmsg)
        else:
            rsltmsg = request.form['holiday'] + "は、祝日マスタに登録されていません"
            flash(rsltmsg)
            return redirect(url_for('home'))
        