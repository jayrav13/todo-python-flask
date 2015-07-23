from flask import Flask, request, render_template, redirect
import requests
from models import Todo, db

app = Flask(__name__)
app.debug = True

@app.route('/', methods=['GET','POST'])
def hello():
	return render_template("todo.html")

@app.route('/add', methods=['POST'])
def add():
	item = Todo()
	
	item.title = request.form["title"]
	item.description = request.form["description"]

	item.add()

	return redirect('/')

@app.route('/delete', methods=['GET'])
def delete():
	item = Todo.query.filter_by(id=request.args['id']).first()
	item.delete()
	return redirect('/') 

@app.route('/edit', methods=['GET','POST'])
def edit():
	if not request.form:
		print "Not form"
	else:
		print "Form"
	return "Hello World"

if __name__ == "__main__":
	app.run()
