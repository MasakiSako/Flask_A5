from flask_blog import app

# Readme: server.pyが直接実行されたときに実行
if __name__ == '__main__':
    app.run(debug = True)