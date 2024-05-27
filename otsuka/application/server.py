#起動ファイルの作成
#最初にappをインポートする
from flask_blog import app

#ファイルが直接実行されたときに実行される処理
if __name__ =='__main__':
    #デバックモードでアプリケーションを起動
    app.run()