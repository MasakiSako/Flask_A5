from flask_blog.models.entries import Entry
from flask_blog import db

from flask import request, redirect, url_for, render_template, flash, session
from flask_blog import app
from flask_blog.views.views import login_required

# Do: Create_Add-New-Entry(View)
@app.route('/')
@login_required
def show_entries():
    # Do: Read_get-data-from-table
    entries = Entry.query.order_by(Entry.id.desc()).all()
    return render_template('entries/index.html', entries=entries)

# Create:new-blog
@app.route('/entries', methods=['POST'])
@login_required
def add_entry():
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
@login_required
def new_entry():
    return render_template('entries/new.html')

# Read:Created-Blog
@app.route('/entries/<int:id>', methods=['GET'])
@login_required
def show_entry(id):
    entry = Entry.query.get(id)
    return render_template('entries/show.html', entry=entry)

# Update:編集ボタンを押したときの挙動
@app.route('/entries/<int:id>/edit', methods=['GET'])
@login_required
def edit_entry(id):
    entry = Entry.query.get(id)
    return render_template('entries/edit.html', entry=entry)

# Update:編集を保存ボタンを押したときの挙動
@app.route('/entries/<int:id>/update', methods=['POST'])
@login_required
def update_entry(id):
    entry = Entry.query.get(id)
    entry.title = request.form['title']
    entry.text = request.form['text']

    # Update:except-same-title
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

# Delete:削除ボタンを押したときの挙動
@app.route('/entries/<int:id>/delete', methods=['POST'])
@login_required
def delete_entry(id):
    entry = Entry.query.get(id)
    db.session.delete(entry)
    db.session.commit()
    flash("投稿が削除されました")
    return redirect(url_for('show_entries'))