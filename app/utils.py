import datetime
from google.cloud import datastore

datastore_client = datastore.Client()


class Datastore:

    def __init__(self, key):
        self.key = key
        

    def _fetch_all(self, status):
        query = datastore_client.query(kind=self.key)
        query.add_filter('status', '=', status)
        # query.order = ['-timestamp']
        return query.fetch()

    def _add(self, description):
        todo_entity = datastore.Entity(key=datastore_client.key(self.key))
        todo_entity.update({
            'description': description,
            'status': False,
            'timestamp': datetime.datetime.now(),
        })
        datastore_client.put(todo_entity)
        return todo_entity

    def _remove(self, todo_id):
        key = datastore_client.key(self.key, int(todo_id))
        datastore_client.delete(key)

    def _mark(self, todo_id, status):
        key = datastore_client.key(self.key, int(todo_id))
        task = datastore_client.get(key)
        task['status'] = bool(int(status))
        datastore_client.put(task)
