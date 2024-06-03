from flask import request, redirect, url_for, render_template, flash, session
from attendance import app
from attendance import db
from attendance.models.entries import Entry
from attendance.views.login import login_required

@app.route('/list', methods=['POST'])
@login_required
def show_a10z():
    date=request.form['inputdate']
    entries = Entry.query.filter_by(date=date).all() 
    entriesnum = Entry.query.filter_by(date=date).count() 
    return render_template('list.html',entries=entries,datem=date,amount=entriesnum)