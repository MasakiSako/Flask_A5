from zoneinfo import ZoneInfo
from flask_blog import db
from datetime import datetime

class Entry(db.Model):
    # Do: SQL(CREATE TABLE)
    __tablename__ = 'entries'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=True)
    text = db.Column(db.Text)
    created_at = db.Column(db.DateTime)

    # Do: Default-Program(Created-Model) 
    def __init__(self, title=None, text=None):
        self.title = title
        self.text = text
        # Add: Datetime-in-JPN
        self.created_at = datetime.now(ZoneInfo("Asia/Tokyo"))
        

    # Do: Export-Format(Read-Model)
    def __repr__(self):
        return '<Entry id:{} title:{} text:{}>'.format(self.id, self.title, self.text)
