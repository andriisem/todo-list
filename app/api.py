from flask import render_template, request
from app import app, db


@app.route('/')
def index():
    all_uncompleted = db._fetch_all(status=False)
    all_completed = db._fetch_all(status=True)
    return render_template('index.html',
                           title='To Do',
                           all_uncompleted=all_uncompleted,
                           all_completed=all_completed
                           )


@app.route('/_add')
def add():
    description = request.args.get('description')
    q = db._add(description)
    todo = "<li id='%s'><input type='checkbox' id='%s'> %s <i class='fa fa-trash removeTask' id='%s'></i></li>" % (
        q.id, q.id, description, q.id)
    return todo


@app.route('/_remove')
def remove():
    todo_id = request.args.get('id')
    db._remove(todo_id)
    return {}


@app.route('/_mark')
def mark():
    status = request.args.get('status')
    todo_id = request.args.get('id')
    db._mark(todo_id, status)
    return {}
