from flask_blog import app

# Readme: / にリクエストがあった時の処理
@app.route("/")
def show_entries():
    return "Hello World!"