from flask import render_template, request
from app import app

from google.cloud import datastore


datastore_client = datastore.Client()


def _add(description):
	todo_list_entity = datastore.Entity(key=datastore_client.key('todo_list'))
	todo_list_entity.update({
        'description': description,
        'status': False,
    })
	datastore_client.put(todo_list_entity)
	return todo_list_entity

def _remove(todo_id, datastore_client):
	key = datastore_client.key('todo_list', int(todo_id))
	print(key)
	datastore_client.delete(key)
	return 


@app.route('/')
def index():
	query = datastore_client.query(kind='todo_list')
	times = query.fetch()
	return render_template('index.html', 
		title='To Do', 
		times=times)

@app.route('/_add')
def add():
	description = request.args.get('description')
	q = _add(description)
	todo = "<li id='%s'><input type='checkbox' id='%s'> %s <i class='fa fa-trash removeTask' id='%s'></i></li>" % (q.id, q.id, description, q.id)
	return todo 


@app.route('/_remove')
def remove():
	todo_id = request.args.get('id')
	_remove(todo_id, datastore_client)
	return {}


@app.route('/_mark')
def mark():
	status = request.args.get('status')
	todo_id = request.args.get('id')
	todo = models.Tasks.query.get(todo_id)
	todo.status = int(status)
	db.session.commit()
	return {}
