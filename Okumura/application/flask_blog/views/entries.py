from flask_blog.models.entries import Entry
from flask_blog import db

from flask import request, redirect, url_for, render_template, flash, session
from flask_blog import app

# Do: Create_Add-New-Entry(View)
@ app.route('/')
def show_entries():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    # Do: Read_get-data-from-table
    entries = Entry.query.order_by(Entry.id.desc()).all()
    return render_template('entries/index.html', entries=entries)

# Create:new-blog
@app.route('/entries', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    
    entry = Entry(
        title = request.form['title'],
        text = request.form['text']
    )
    db.session.add(entry)
    # Update_except-same-title
    try:
        db.session.commit()
        flash('新しく記事が作成されました')
        return redirect(url_for('show_entries'))
    except:
        flash('タイトル名がすでに存在しています')
        return redirect(url_for('new_entry'))


@app.route('/entries/new', methods=["GET"])
def new_entry():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('entries/new.html')

# Read:Created-Blog
@app.route('/entries/<int:id>', methods=['GET'])
def show_entry(id):
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    entry = Entry.query.get(id)
    return render_template('entries/show.html', entry=entry)

# Update: 編集ボタンを押したときの挙動
@app.route('/entries/<int:id>/edit', methods=['GET'])
def edit_entry(id):
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    entry = Entry.query.get(id)
    return render_template('entries/edit.html', entry=entry)

# Update: 編集を保存ボタンを押したときの挙動
@app.route('/entries/<int:id>/update', methods=['POST'])
def update_entry(id):
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    entry = Entry.query.get(id)
    entry.title = request.form['title']
    entry.text = request.form['text']

    # Update_except-same-title
    try:
        db.session.merge(entry)
        db.session.commit()
        flash("記事が更新されました")
        return redirect(url_for('show_entries'))
    except:
        flash('タイトル名がすでに存在しています')
        return redirect(url_for('show_entries'))
        # Todo: できれば、edit_entryにリダイレクトしたい(編集データを引き渡せていないためエラー)
        # return redirect(url_for('edit_entry',entry=entry))