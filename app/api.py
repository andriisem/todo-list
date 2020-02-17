import json
from flask import jsonify, request
from app import app, db


@app.route('/get', methods=['GET'])
def get():
    return jsonify(db._fetch_all())
    

@app.route('/add', methods=['POST'])
def add():
    response = json.loads(request.get_data())
    description = response['description']
    new_task = db._add(description)
    return jsonify({'description': description, 'id': new_task.id, 'status': False})


@app.route('/remove', methods=['DELETE'])
def remove():
    response = json.loads(request.get_data())
    todo_id = response['todo_id']
    db._remove(todo_id)
    return jsonify({'id': todo_id})


@app.route('/mark', methods=['PUT'])
def mark():
    response = json.loads(request.get_data())
    todo_id = response['todo_id']
    status = response['status']
    db._mark(todo_id, status)
    return jsonify({'id': todo_id, 'status': status})
