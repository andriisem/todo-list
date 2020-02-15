from flask import render_template, request
from app import app, models, db


@app.route('/')
def index():
	todo_list = models.Tasks.query.all()
	return render_template('index.html', title='To Do', todo_list=todo_list)


@app.route('/_add')
def add():
	description = request.args.get('description')
	test = models.Tasks(description=description)
	db.session.add(test)
	db.session.commit()
	todo = "<li id='%s'><input type='checkbox'> %s <i class='fa fa-trash' onclick='removeTask(%s)'></i></li>" % (test.id, description, test.id)
	return todo 


@app.route('/_delete')
def delete():
	todo_id = request.args.get('id')
	todo = models.Tasks.query.get(todo_id)
	db.session.delete(todo)
	db.session.commit()
	return {}
