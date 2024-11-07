from flask import Response, json, jsonify
from datetime import datetime
import random
from marshmallow import ValidationError
from .db import *
from .entities import *
from . import app

names = {"Alan", "Bob", "Rufus", "Blayd"}
names_category = {"food", "car", "ticket", "water"}

user_id = 1
user_schema = PlainUserSchema()

category_id = 1
category_schema = PlainCategorySchema()

record_id = 1
record_schema = PlainRecordSchema()

@app.route("/", methods=["GET"])
def healthcheck():
    return Response(json.dumps({
            "Status": "200", 
            "Time": datetime.now().isoformat()
        }, indent=4), mimetype='application/json'), 200

# User request
@app.route("/user/<int:Id>", methods=["GET"])
def get_user(Id):
    try:
        user = UserModel.query.get(Id)
        if user is None:
            return "User not found", 404 
        return Response(json.dumps({
                'Id': user.Id,
                'Name': user.Name
            }, indent=4), mimetype='application/json'), 200
    except Exception as err:
        db.session.rollback()
        return f"{err}", 422

@app.route("/user", methods=["POST"])
def create_user():
    try:
        global user_id
        global names
        new_user = user_schema.load({
                'Id': user_id, 
                'Name': random.choice(list(names))
            })
        new_user = UserModel(
                Id=new_user["Id"],
                Name=new_user["Name"]
            )
        db.session.add(new_user)
        db.session.commit()
        user_id += 1
        return "User create", 200
    except ValidationError as err:
        return f"{err}]", 422
    except Exception as err:
        db.session.rollback()
        return f"{err}", 422

@app.route("/user/<int:Id>", methods=["DELETE"])
def delete_user(Id):
    try:
        user = UserModel.query.get(Id)
        if user is None:
            return "User not found", 404
        db.session.delete(user)
        db.session.commit()
        return "User delete", 200
    except Exception as err:
        db.session.rollback()
        return f"{err}", 422

@app.route("/users", methods=["GET"])
def show_user():
    try:
        users = UserModel.query.all()
        users_dict = {}
        index = 0
        for user in users:
            users_dict[index] = {
                    'Id': user.Id,
                    'Name': user.Name,
                }
            index +=1
        return Response(json.dumps(users_dict, indent=4), mimetype='application/json'), 200
    except Exception as err:
        db.session.rollback()
        return f"{err}", 422

# Category request
@app.route("/category", methods=["GET"])
def get_category():
    try:
        categorys = CategoryModel.query.all()
        categorys_dict = {}
        index = 0
        for category in categorys:
            categorys_dict[index] = {
                    'Id': category.Id,
                    'Name': category.Name,
                }
            index +=1
        return jsonify(categorys_dict), 200
    except Exception as err:
        db.session.rollback()
        return f"{err}", 422

@app.route("/category", methods=["POST"])
def create_category():
    try:
        global category_id
        global names_category
        new_category = category_schema.load({
                'Id': category_id,
                'Name': random.choice(list(names_category))
            })
        new_category = CategoryModel(
                Id=new_category["Id"],
                Name=new_category["Name"]
            )
        db.session.add(new_category)
        db.session.commit()
        category_id += 1
        return "Category create", 200
    except ValidationError as err:
        return f"{err}]", 422
    except Exception as err:
        db.session.rollback()
        return f"{err}", 422

@app.route("/category/<int:Id>", methods=["DELETE"])
def delete_category(Id):
    try:
        category = CategoryModel.query.get(Id)
        if category is None:
            return "Category not found", 404
        db.session.delete(category)
        db.session.commit()
        return "Category delete", 200
    except Exception as err:
        db.session.rollback()
        return f"{err}", 422

#Record request
@app.route("/records", methods=["GET"])
def get_records():
    try:
        records = RecordModel.query.all()
        records_dict = {}
        index = 0
        for record in records:
            records_dict[index] = {
                    'Id': record.Id,
                    'User_id': record.User_id,
                    'Category_id': record.Category_id,
                    'Time': record.Time,
                    'Pay': record.Pay
                }
            index +=1
        return Response(json.dumps(records_dict, indent=4), mimetype='application/json'), 200
    except Exception as err:
        db.session.rollback()
        return f"{err}", 422

@app.route("/record/<int:Id>", methods=["GET"])
def get_record(Id):
    try:
        record = RecordModel.query.get(Id)
        if record is None:
            return "Record not found", 404
        return Response(json.dumps({
                'Id': record.Id,
                'User_id': record.User_id,
                'Category_id': record.Category_id,
                'Time': record.Time,
                'Pay': record.Pay
            }, indent=4), mimetype='application/json'), 200
    except Exception as err:
        db.session.rollback()
        return f"{err}", 422

@app.route("/record/<path:params>", methods=["POST"])
def create_record(params):
    try:
        if len(params.split("-")) != 2:
            return "Parameters is not two", 404

        user_id, category_id = params.split('-')

        if not user_id or not category_id:
            return "Parameters have not", 404

        if not user_id.isdigit() or not category_id.isdigit():
            return "Parameters must be numbers", 404

        user_id = int(user_id)
        user = UserModel.query.get(user_id)
        if user is None:
            return "User not found. Record not create", 404
        category_id = int(category_id)
        category = CategoryModel.query.get(category_id)
        if category is None:
            return "<Сategory not found. Record not create", 404

        global record_id
        new_record = record_schema.load({
                "Id": record_id,
                "User_id": user_id,
                "Category_id": category_id,
                "Time": datetime.now().isoformat(),
                "Pay": random.randint(1, 100),
            })
        new_record = RecordModel(
                Id=new_record["Id"],
                User_id=new_record["User_id"],
                Category_id=new_record["Category_id"],
                Time=new_record["Time"],
                Pay=new_record["Pay"]
            )
        db.session.add(new_record)
        db.session.commit()
        record_id += 1
        return "Record create", 200
    except ValidationError as err:
        return f"{err}]", 422
    except Exception as err:
        db.session.rollback()
        return f"{err}", 422

@app.route("/record/<int:Id>", methods=["DELETE"])
def delete_record(Id):
    try:
        record = RecordModel.query.get(Id)
        if record is None:
            return "Record not found", 404
        db.session.delete(record)
        db.session.commit()
        return "Record delete", 200
    except Exception as err:
        db.session.rollback()
        return f"{err}", 422

@app.route("/record/<path:params>", methods=["GET"])
def show_record(params):
    try:
        if len(params.split("-")) != 2:
            return "Parameters is not two", 404

        user_id, category_id = params.split('-')

        if not user_id or not category_id:
            return "Parameters have not", 404

        if not user_id.isdigit() or not category_id.isdigit():
            return "Parameters must be numbers", 404

        user_id = int(user_id)
        category_id = int(category_id)

        results = RecordModel.query.filter(
            (RecordModel.User_id == user_id) | (RecordModel.Category_id == category_id)
        ).all()

        if not results:
            return "Record not found", 404
    
        results_dict = {}
        index = 0
        for result in results:
            results_dict[index] = {
                    'Id': result.Id,
                    'User_id': result.User_id,
                    'Category_id': result.Category_id,
                    'Time': result.Time,
                    'Pay': result.Pay
                }
            index +=1

        return Response(json.dumps(results_dict, indent=4), mimetype='application/json'), 200
    
    except Exception as err:
        db.session.rollback()
        return f"{err}", 422