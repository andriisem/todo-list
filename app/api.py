from flask import render_template, request, jsonify
from app import app, db


@app.route('/get', methods=['GET'])
def get():
    return jsonify(db._fetch_all())
    

@app.route('/add')
def add():
    description = request.args.get('description')
    new_task = db._add(description)
    return jsonify({'description': description, 'id': new_task.id})


@app.route('/remove')
def remove():
    todo_id = request.args.get('todo_id')
    db._remove(todo_id)
    return jsonify({'id': todo_id})


@app.route('/mark')
def mark():
    status = request.args.get('status')
    todo_id = request.args.get('id')
    db._mark(todo_id, status)
    return jsonify({'id': todo_id, 'status': status})
