from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/test'
db = SQLAlchemy(app)

class Todo(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String)
	description = db.Column(db.String)	

	def __init__(self, title, description):
		self.title = title
		self.description = description
		return None

	def add(self):
		db.session.add(self)
		db.session.commit()

	def delete(self):
		db.session.delete(self)
		db.session.commit()	

	def edit(self, title, description):
		self.title = title
		self.description = description
		
	def __repr__(self):
		return '%s:%s' % (self.title, self.description)
