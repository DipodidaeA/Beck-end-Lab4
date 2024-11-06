from flask import Flask
from flask_migrate import Migrate

app = Flask(__name__)

from .views import *
from .db import db

migrate = Migrate(app, db)