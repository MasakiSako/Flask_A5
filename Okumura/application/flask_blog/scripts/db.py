from flask_script import Command
from flask_blog import db
from flask_blog.models.entries import Entry

class InitDB(Command):
    "create database"

    def run(self):
        db.create_all()