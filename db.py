from . import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

app.config.from_pyfile('config.py', silent=True)

db.init_app(app)

class UserModel(db.Model):
    __tablename__ = "user"

    Id = db.Column(db.Integer, primary_key = True)
    Name = db.Column(db.String(128), unique=True, nullable=False)

    record = db.relationship("RecordModel", back_populates="user", lazy="dynamic")

class CategotyModel(db.Model):
    __tablename__ = "category"

    Id = db.Column(db.Integer, primary_key = True)
    Name = db.Column(db.String(128), unique=True, nullable=False)

    record = db.relationship("RecordModel", back_populates="category", lazy="dynamic")

class RecordModel(db.Model):
    __tablename__ = "record"

    Id = db.Column(db.Integer, primary_key = True)
    User_id = db.Column(db.Integer, db.ForeingKey("user.Id"), unique=False, nullable=False)
    Category_id = db.Column(db.Integer, db.ForeingKey("category.Id"), unique=False, nullable=False)
    Time = db.Column(db.String, nullable=False)
    Pay = db.Column(db.Integer, nullable=False)

    user = db.relationship("UserModel", back_populates="record")
    category = db.relationship("CategoryModel", back_populates="record")