from flask import request, redirect, url_for, render_template, flash, session
from holiday import app
from holiday import db
from holiday.models.mst_holiday import Entry


@app.route('/list', methods=['POST'])
def show_holidays():
    entries = Entry.query.order_by(Entry.holi_date.desc()).all()
    return render_template('list.html',entries=entries)