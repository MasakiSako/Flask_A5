from zoneinfo import ZoneInfo
from holiday import db
from datetime import datetime

class Holiday(db.Model):
    # Do: SQL(CREATE TABLE)
    __tablename__ = 'holiday'
    holi_date = db.Column(db.Date, primary_key=True)
    holi_text = db.Column(db.String(20))

    # Do: Default-Program(Created-Model) 
    def __init__(self, title=None, text=None):
        self.title = title
        self.text = text
        # Add: Datetime-in-JPN
        self.created_at = datetime.now(ZoneInfo("Asia/Tokyo"))
        

    # Do: Export-Format(Read-Model)
    def __repr__(self):
        return '<Entry id:{} title:{} text:{}>'.format(self.id, self.title, self.text)
