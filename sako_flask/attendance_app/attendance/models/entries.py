from attendance import db
class Entry(db.Model):
    __tablename__ = 'attendances'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    date = db.Column(db.Date)

    def __init__(self, name=None, date=None):
        self.name = name
        self.date = date
    
    def __repr__(self):
        return '<Entry id:{} name:{} date:{}>'.format(self.id, self.name, self.date)
    
class NameList(db.Model):
    __tablename__ = 'nameList'
    name = db.Column(db.String(30), primary_key=True)
    logpass = db.Column(db.String(20))
    isMaster = db.Column(db.String(2))

    def __init__(self, name=None, logpass=None, isMaster=None):
        self.name = name
        self.logpass =logpass
        self.isMaster = isMaster
        
    def __repr__(self):
        return '<NameList name:{}>'.format(self.name)