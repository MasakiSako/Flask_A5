from flask_script import Command
from attendance import db
from attendance.models.entries import Entry , NameList

class InitDB(Command):
    "create database"

    def run(self):
        db.create_all()