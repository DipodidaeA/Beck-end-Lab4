from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
migrate = Migrate()

app = Flask(__name__)

app.config.from_pyfile('config.py', silent=True)

db.init_app(app)

migrate.init_app(app, db)

jwt = JWTManager(app)

from .views import *