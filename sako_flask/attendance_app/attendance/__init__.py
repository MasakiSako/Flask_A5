from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('attendance.config')

db=SQLAlchemy(app)
from attendance.views import list,login,master