from flask import request, redirect, url_for, render_template, flash, session
from holiday import app
from holiday import db
from holiday.models.mst_holiday import Entry

@app.route('/maintenance_data', methods=['POST'])
def new_entry():
    # Create
    # Todo: Update
    if request.form["button"] == "insert_update":
        entry = Entry(
            holi_date = request.form['date'],
            holi_text = request.form['text']
        )
        db.session.add(entry)
        db.session.commit()
        message = str(entry.holi_text) + "が登録されました"
        return render_template('entries/maintenance_date.html', message = message)
    # Delete:削除ボタンを押したときの挙動
    elif request.form["button"] == "delete":
        holi_date = request.form['date']
        
        entry = Entry.query.get(holi_date)
        
        db.session.delete(entry)
        db.session.commit()
        message = str(entry.holi_text) + "が削除されました"
        return render_template('entries/maintenance_date.html', entry=entry)