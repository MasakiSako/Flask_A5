# チェックリスト
1. サーバー起動編
   1. server.py
    - [-] タイプミスがない
    - [-] '__main__' のアンダースコアは各２つずつ
   2. appの用意
    - [-] アプリケーション本体（テキストで言うflask_appフォルダ）を作成した
    - [-] 直下に__init__.pyを作成した
      - [-] flaskをimportした
      - [-] appを定義した
   3. templatesの用意
    - [-] アプリケーション本体フォルダ内にtemplatesフォルダを作成した
    - [-] タイプミスがない
    - [-] 適当な名前でhtmlファイルを作成した（中身も適当でOK）
   4. configファイルの用意
    - [-] アプリケーション本体フォルダ内にconfig.pyを作成した
    - [-] `DEBUG=True`を記載した
   5. viewsの用意
    - [-] アプリケーション本体フォルダ内にviewsファイルを作成した
    - [-] appとrender_templateをimportした
    - [-] `@app.route('/')`とそれに紐づく関数を定義した
      - [-] `render_template`で、3.で用意したhtmlファイルをreturnするようにした
   6. 起動準備
    - [-] アプリケーション本体の__init__.pyでconfigを読み込んでいる
    - [-] アプリケーション本体の__init__.pyでviewsを読み込んでいる（同一ディレクトリにviews.pyが存在する場合、`from .views import *`のようになる）
    - [-] server.pyでアプリケーション本体をimportしている
   7. 起動
    - [-] `python server.py`を実行するフォルダが適切である
       - [-] `pwd`で自分の作業ディレクトリであることを確認した
       - [-] `ls`で現在のディレクトリにserver.pyが配置されているのを確認した
    - [-] `python server.py`を実行する 

## トラブルシューティング
- 404 Not Foundが出た
  - 5.の内容を確認してください
- SyntaxErrorが出た
  - タイプミスの可能性が高いです。エラーメッセージ指摘箇所の記述を一文字ずつ確認してください
- TemplateNotFoundが出た
  - 3.と5.の内容を確認してください
- server.pyを実行しても何も起きない
  - 1.の内容を確認してください