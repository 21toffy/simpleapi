from flask_sqlalchemy import SQLAlchemy

from main import app
from datetime import datetime
from time import time
import os

db = SQLAlchemy(app)


app.config['SECRET_KEY'] = 'simpleapi'


basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, "db.sqlite") + 'simpleapi.db'



class Post (db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title =db.Column(db.String(140))
	body = db.Column(db.Text)
	created = db.Column(db.DateTime, default=datetime.now())


