from flask_script import Command
from holiday import db
from holiday import Entry

class InitDB(Command):
    "create database"

    def run(self):
        db.create_all()