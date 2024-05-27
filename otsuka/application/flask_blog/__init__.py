#アプリケーション本体ファイルの作成
#Flask自体をインポート
from flask import Flask

#flaskのアプリケーション本体を作成
app = Flask(__name__)

#flask_blogフォルダ以下にあるconfig.pyの内容をconfigとして扱う
app.config.from_object('flask_blog.config')

#これから作成する「views」というファイルをインポート
import flask_blog.views