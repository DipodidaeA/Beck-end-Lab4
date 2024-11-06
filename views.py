from flask import jsonify
from datetime import datetime
import random

from marshmallow import ValidationError
from . import app, entities
from . import db, UserModel, CategotyModel, RecordModel

class User:
    def __init__(self, Id: int, Name: str):
        self.Id = Id
        self.Name = Name
    
    def to_dict(self):
        return {"Id": self.Id, "Name": self.Name}

class Category:
    def __init__(self, Id: int, Name: str):
        self.Id = Id
        self.Name = Name
    
    def to_dict(self):
        return {"Id": self.Id, "Name": self.Name}

class Record:
    def __init__(self, Id: int, User_id: int, Category_id: int, Time: str, Pay: int):
        self.Id = Id
        self.User_id = User_id
        self.Category_id = Category_id
        self.Time = Time
        self.Pay = Pay

    def to_dict(self):
        return {"Id": self.Id, "User_id": self.User_id, "Category_id": self.Category_id, "Time": self.Time, "Pay": self.Pay}

names = {"Alan", "Bob", "Rufus", "Blayd"}
names_category = {"food", "car", "ticket", "water"}

user_id = 1
user_schema = entities.PlainUserSchema()

category_id = 1
category_schema = entities.PlainCategorySchema()

record_id = 1
record_schema = entities.PlainRecordSchema()

@app.route("/", methods=["GET"])
def healthcheck():
    response = {
        "status": "200",
        "date": datetime.now().isoformat()
    }
    return jsonify(response), 200

# User request
@app.route("/user/<int:Id>", methods=["GET"])
def get_user(Id):
    try:
        user = UserModel.query.get(Id-1)
        if user is None:
            return "<p>User not found</p>", 404 
        return jsonify(user), 200
    except Exception as err:
        db.session.rollback()
        return f"<p>{err}</p>", 422

@app.route("/user", methods=["POST"])
def create_user():
    try:
        global user_id
        global names
        new_user = User(user_id, random.choice(list(names))).to_dict()
        new_user = user_schema.load(new_user)
        new_user = UserModel(new_user)
        db.session.add(new_user)
        db.session.commit()
        user_id += 1
        return "<p>User create</p>", 200
    except ValidationError as err:
        return f"<p>{err}]</p>", 422
    except Exception as err:
        db.session.rollback()
        return f"<p>{err}</p>", 422

@app.route("/user/<int:Id>", methods=["DELETE"])
def delete_user(Id):
    try:
        user = UserModel.query.get(Id-1)
        if user is None:
            return "<p>User not found</p>", 404
        db.session.delete(user)
        db.session.commit()
        return "<p>User delete</p>", 200
    except Exception as err:
        db.session.rollback()
        return f"<p>{err}</p>", 422

@app.route("/users", methods=["GET"])
def show_user():
    try:
        users = UserModel.query.all()
        return jsonify([user.to_dict() for user in users]), 200
    except Exception as err:
        db.session.rollback()
        return f"<p>{err}</p>", 422

# Category request
@app.route("/category", methods=["GET"])
def get_category():
    try:
        categorys = CategotyModel.query.all()
        return jsonify([category.to_dict() for category in categorys]), 200
    except Exception as err:
        db.session.rollback()
        return f"<p>{err}</p>", 422

@app.route("/category", methods=["POST"])
def create_category():
    try:
        global category_id
        global names_category
        new_category = Category(category_id, random.choice(list(names_category))).to_dict()
        new_category = category_schema.load(new_category)
        new_category = CategotyModel(new_category)
        db.session.add(new_category)
        db.session.commit()
        category_id += 1
        return "<p>Category create</p>", 200
    except ValidationError as err:
        return f"<p>{err}]</p>", 422
    except Exception as err:
        db.session.rollback()
        return f"<p>{err}</p>", 422

@app.route("/category/<int:Id>", methods=["DELETE"])
def delete_category(Id):
    try:
        category = CategotyModel.query.get(Id-1)
        if category is None:
            return "<p>Category not found</p>", 404
        db.session.delete(category)
        db.session.commit()
        return "<p>Category delete</p>", 200
    except Exception as err:
        db.session.rollback()
        return f"<p>{err}</p>", 422

#Record request
@app.route("/records", methods=["GET"])
def get_records():
    try:
        records = RecordModel.query.all()
        return jsonify([record.to_dict() for record in records]), 200
    except Exception as err:
        db.session.rollback()
        return f"<p>{err}</p>", 422

@app.route("/record/<int:Id>", methods=["GET"])
def get_record(Id):
    try:
        record = RecordModel.query.get(Id-1)
        if record is None:
            return "<p>Record not found</p>", 404
        return jsonify(record), 200
    except Exception as err:
        db.session.rollback()
        return f"<p>{err}</p>", 422

@app.route("/record", methods=["POST"])
def create_record():
    try:
        global record_id
        global user_id
        global category_id
        new_record = Record(record_id, user_id-1, category_id-1, datetime.now().isoformat(), random.randint(1, 100)).to_dict()
        new_record = record_schema.load(new_record)
        new_record = RecordModel(new_record)
        db.session.add(new_record)
        db.session.commit()
        record_id += 1
        return "<p>Record create</p>", 200
    except ValidationError as err:
        return f"<p>{err}]</p>", 422
    except Exception as err:
        db.session.rollback()
        return f"<p>{err}</p>", 422

@app.route("/record/<int:Id>", methods=["DELETE"])
def delete_record(Id):
    try:
        record = RecordModel.query.get(Id-1)
        if record is None:
            return "<p>Category not found</p>", 404
        db.session.delete(record)
        db.session.commit()
        return "<p>Record delete</p>", 200
    except Exception as err:
        db.session.rollback()
        return f"<p>{err}</p>", 422

@app.route("/record/<path:params>", methods=["GET"])
def show_record(params):
    try:
        if len(params.split("-")) != 2:
            return "<p>Parameters is not two</p>", 404

        user_id, category_id = params.split('-')

        if not user_id or not category_id:
            return "<p>Parameters have not</p>", 404

        if not user_id.isdigit() or not category_id.isdigit():
            return "<p>Parameters must be numbers</p>", 404

        user_id = int(user_id)
        category_id = int(category_id)

        results = RecordModel.query.filter(
            (RecordModel.User_id == user_id) | (RecordModel.Category_id == category_id)
        ).all()

        if not results:
            return "<p>Record not found</p>", 404
    
        results = [record.to_dict() for record in results]

        return jsonify(results), 200
    except Exception as err:
        db.session.rollback()
        return f"<p>{err}</p>", 422