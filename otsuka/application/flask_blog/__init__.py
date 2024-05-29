from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('flask_blog.config')

db = SQLAlchemy(app)

#import otsuka.application.flask_blog.views.views

from flask_blog.views import views, entries