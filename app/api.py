from flask import jsonify
from app import app, db


@app.route('/get', methods=['GET'])
def get():
    return jsonify(db._fetch_all())
    

@app.route('/add/<description>', methods=['POST'])
def add(description):
    new_task = db._add(description)
    return jsonify({'description': description, 'id': new_task.id})


@app.route('/remove/<todo_id>', methods=['POST'])
def remove(todo_id):
    db._remove(todo_id)
    return jsonify({'id': todo_id})


@app.route('/mark/<todo_id>/<status>', methods=['POST'])
def mark(todo_id, status):
    db._mark(todo_id, status)
    return jsonify({'id': todo_id, 'status': status})
