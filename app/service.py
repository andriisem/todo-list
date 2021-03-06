import datetime
from google.cloud import datastore


class Datastore:
    def __init__(self, db_name, datastore_client):
        self.db_name = db_name
        self.datastore_client = datastore_client

    def _fetch_all(self):
        result = []
        query = self.datastore_client.query(kind=self.db_name)
        query.order = ['timestamp']
        for task in query.fetch():
            result.append({
                'id': task.key.id,
                'description': task.get('description'),
                'status': 'checked' if task.get('status') else '',
                'timestamp': task.get('timestamp'),
            })
        return {'result': result}

    def _add(self, description):
        todo_entity = datastore.Entity(key=self.datastore_client.key(self.db_name))
        todo_entity.update({
            'description': description,
            'status': False,
            'timestamp': datetime.datetime.now(),
        })
        self.datastore_client.put(todo_entity)
        return todo_entity

    def _remove(self, todo_id):
        key = self.datastore_client.key(self.db_name, int(todo_id))
        self.datastore_client.delete(key)

    def _mark(self, todo_id, status):
        key = self.datastore_client.key(self.db_name, int(todo_id))
        task = self.datastore_client.get(key)
        task['status'] = bool(int(status))
        self.datastore_client.put(task)
