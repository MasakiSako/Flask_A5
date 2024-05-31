from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('holiday.config')

# Setting DB
db = SQLAlchemy(app)

from holiday.views import views, enties