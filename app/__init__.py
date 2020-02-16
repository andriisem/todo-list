from flask import Flask
from app.utils import Datastore

app = Flask(__name__)
db = Datastore('todo_list')

from app import api
