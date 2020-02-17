from flask import Flask
from app.service import Datastore
from google.cloud import datastore

app = Flask(__name__)
db_name = 'todo_list'
datastore_client = datastore.Client()

db = Datastore(db_name, datastore_client)

from app import api
