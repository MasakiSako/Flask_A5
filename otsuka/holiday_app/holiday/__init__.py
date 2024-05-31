#ここはアプリケーション本体のファイルです。

#Flask自体をインポート
from flask import Flask

#Flaskのアプリケーションを作成
app = Flask(__name__)

#holidayフォルダ以下にあるconfig.pyの内容をconfigとして扱うよ
app.config.from_object('holiday.config')

#viewsというファイルをインポート
import  holiday.views