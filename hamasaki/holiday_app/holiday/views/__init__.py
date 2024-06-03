from holiday import app,db
from flask import request, redirect, url_for, render_template, flash, session
from holiday.models.mst_holiday import Entry

@app.route('/')
def show_entries():
    entries = Entry.query.order_by(Entry.holi_date.desc()).all()
    return render_template('input.html', entries=entries)

@app.route('/maintenance_date', methods=['POST'])
def add_or_update_or_delete_entry():
    

    #新規・更新
    if request.form["button"] == "insert_update":
         entry = Entry(
             holi_date = request.form['holi_date'],
             holi_text = request.form['holi_text']
             )
         entry2 = Entry.query.filter_by(holi_date=entry.holi_date).first()
         if entry2:
             # 既存のエントリーが存在する場合、テキストを更新
             entry.holi_text = request.form['holi_text']
             db.session.commit()
             flash(f'{entry.holi_date} は「{entry.holi_text}」に更新されました')
             return render_template('result.html', entry=entry)
         else:
             # 該当するエントリーが見つからなかった場合、新しいエントリーを作成
             db.session.add(entry)
             db.session.commit()
             flash(f'{entry.holi_date}（{entry.holi_text}）が登録されました')
             return render_template('result.html', entry=entry)
     #削除    
    elif request.form["button"] == "delete":
         get_form_entry = Entry(
             holi_date = request.form['holi_date'],
             holi_text = request.form['holi_text']
             )
         get_form_entry = Entry.query.get(get_form_entry.holi_date)
         db.session.delete(get_form_entry)
         db.session.commit()
         flash('削除されました')
         return render_template('result.html', entry=get_form_entry)
    

@app.route('/list', methods=['GET'])
def list_entries():
    list_entries = Entry.query.order_by(Entry.holi_date.desc()).all()
    return render_template('list.html', entries=list_entries)

    

# @app.route('/maintenance_date', methods=['POST'])
# def update_entry():
#     # 入力された日付を取得
#     holi_date = request.form['holi_date']

#     # 既存のエントリーを日付で検索
#     entry = Entry.query.filter_by(holi_date=holi_date).first()

#     if entry:
#         # 既存のエントリーが存在する場合、テキストを更新
#         entry.holi_text = request.form['holi_text']
#         db.session.commit()
#         flash('記事が更新されました')
#     else:
#         # 該当するエントリーが見つからなかった場合、新しいエントリーを作成
#         entry = Entry(
#             holi_date=holi_date,
#             holi_text=request.form['holi_text']
#         )
#         db.session.add(entry)
#         db.session.commit()
#         flash('新しく記事が作成されました')

#     return render_template('result.html', entry=entry)