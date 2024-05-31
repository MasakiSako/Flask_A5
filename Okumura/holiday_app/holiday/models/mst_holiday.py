from zoneinfo import ZoneInfo
from holiday import db
from datetime import datetime

class Entry(db.Model):
    # Do: SQL(CREATE TABLE)
    __tablename__ = 'holiday'
    holi_date = db.Column(db.Date, primary_key=True)
    holi_text = db.Column(db.String(20))

    # Do: Default-Program(Created-Model) 
    def __init__(self, holi_date=None, holi_text=None):
        self.holi_date = holi_date
        self.holi_text = holi_text

    # Do: Export-Format(Read-Model)
    def __repr__(self):
        return '<Entry date:{} text:{}>'.format(self.holi_date, self.holi_text)
