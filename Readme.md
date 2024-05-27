# 環境構築
## Version

~~~
pip install click==8.0.4\
   Flask==1.1.2\
   Flask-Script==2.0.6\
   Flask-SQLAlchemy==2.5.1\
   greenlet==1.1.2\
   itsdangerous==2.0.1\
   Jinja2==3.0.3\
   MarkupSafe==2.1.1\
   setuptools==54.2.0\
   Werkzeug==2.0.3\
   cryptography==39.0.2
~~~

## ディレクトリ構成
~~~
Flask_NonNankai
    |- Flask_Okumura
        |- application <!-- create: flask_blog -->
            |- Pipfile <!-- 作成不要 -->
            |- Pipfile.lock <!-- 作成不要 -->
            |- server.py
            |- flask_blog
                |- __init__.py
                |- views.py
        |- calcsalary_app // 演習
        |- holiday_app // 演習
        |- hello.py
