from flask import Flask, request, render_template, redirect
import requests
from models import Todo, db

app = Flask(__name__)
app.debug = True

@app.route('/', methods=['GET'])
def hello():
	list = Todo.query.all()
	return render_template("todo.html", list=list)

@app.route('/add', methods=['POST'])
def add():
	item = Todo(request.form["title"], request.form["description"])
	item.add()
	return redirect('/')

@app.route('/delete', methods=['GET'])
def delete():
	if request.args or request.args['id']:
		item = Todo.query.filter_by(id=request.args['id']).first()
		if item:
			item.delete()

		return redirect('/') 

@app.route('/edit', methods=['GET','POST'])
def edit():
	if request.form:
		if request.args and request.args['id']:
			item = Todo.query.filter_by(id=request.args['id']).first()
			item.edit(request.form['title'], request.form['description'])	
	
		return redirect('/')
	else:
		if request.args and request.args['id']:
			item = Todo.query.filter_by(id=request.args['id']).first()
			return render_template("edit.html", item=item)	
		else:
			return redirect('/')


if __name__ == "__main__":
	app.run()
