from flask import render_template, request
from app import app, models, db


@app.route('/')
def index():
	todo_list_complete = models.Tasks.query.filter_by(status=True).all()
	todo_list_incomplete = models.Tasks.query.filter_by(status=False).all()
	return render_template('index.html', 
		title='To Do', 
		todo_list_complete=todo_list_complete,
		todo_list_incomplete=todo_list_incomplete)


@app.route('/_add')
def add():
	description = request.args.get('description')
	test = models.Tasks(description=description)
	db.session.add(test)
	db.session.commit()
	todo = "<li id='%s'><input type='checkbox' id='%s'> %s <i class='fa fa-trash removeTask' id='%s'></i></li>" % (test.id, test.id, description, test.id)
	return todo 


@app.route('/_delete')
def delete():
	todo_id = request.args.get('id')
	todo = models.Tasks.query.get(todo_id)
	db.session.delete(todo)
	db.session.commit()
	return {}


@app.route('/_mark')
def mark():
	status = request.args.get('status')
	todo_id = request.args.get('id')
	todo = models.Tasks.query.get(todo_id)
	todo.status = int(status)
	db.session.commit()
	return {}
