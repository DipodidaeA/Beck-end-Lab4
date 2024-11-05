from flask import jsonify
from datetime import datetime
import random
from . import app

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
    def __init__(self, Id: int, user_id: int, category_id: int, time: str, pay: int):
        self.Id = Id
        self.user_id = user_id
        self.category_id = category_id
        self.time = time
        self.pay = pay

    def to_dict(self):
        return {"Id": self.Id, "User_id": self.user_id, "Category_id": self.category_id, "Time": self.time, "Pay": self.pay}

user_id = 1
users = {}

category_id = 1
categorys = {}

record_id = 1
records = {}

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
    if users.get(Id-1) is None:
        return "<p>User not found</p>", 404 
    return jsonify(users.get(Id-1)), 200

@app.route("/user", methods=["POST"])
def create_user():
    global user_id
    new_user  = User(user_id, "Name")
    users[user_id-1] = new_user.to_dict()
    user_id += 1
    return "<p>User create</p>", 200

@app.route("/user/<int:Id>", methods=["DELETE"])
def delete_user(Id):
    if users.get(Id-1) is None:
        return "<p>User not found</p>", 404
    del users[Id-1]
    return "<p>User delete</p>", 200

@app.route("/users", methods=["GET"])
def show_user():
    return jsonify(users), 200

# Category request
@app.route("/category", methods=["GET"])
def get_category():
    return jsonify(categorys), 200

@app.route("/category", methods=["POST"])
def create_category():
    global category_id
    new_category = Category(category_id, "Name")
    categorys[category_id-1] = new_category.to_dict()
    category_id += 1
    return "<p>Category create</p>", 200

@app.route("/category/<int:Id>", methods=["DELETE"])
def delete_category(Id):
    if categorys.get(Id-1) is None:
        return "<p>Category not found</p>", 404
    del categorys[Id-1]
    return "<p>Category delete</p>", 200

#Record request
@app.route("/records", methods=["GET"])
def get_records():
    return jsonify(records), 200

@app.route("/record/<int:Id>", methods=["GET"])
def get_record(Id):
    if records.get(Id-1) is None:
        return "<p>Record not found</p>", 404
    return jsonify(records.get(Id-1)), 200

@app.route("/record", methods=["POST"])
def create_record():
    global record_id
    global user_id
    global category_id
    new_record = Record(record_id, user_id-1, category_id-1, datetime.now().isoformat(), random.randint(1, 50))
    records[record_id-1] = new_record.to_dict()
    record_id += 1
    return "<p>Record create</p>", 200

@app.route("/record/<int:Id>", methods=["DELETE"])
def delete_record(Id):
    if records.get(Id-1) is None:
        return "<p>Record not found</p>", 404
    del records[Id-1]
    return "<p>Record delete</p>", 200

@app.route("/record/<path:params>", methods=["GET"])
def show_record(params):
    if len(params.split("-")) != 2:
        return "<p>Parameters is not two</p>", 404

    user_id, category_id = params.split('-')

    if not user_id or not category_id:
        return "<p>Parameters have not</p>", 404

    if not user_id.isdigit() or not category_id.isdigit():
        return "<p>Parameters must be numbers</p>", 404

    user_id = int(user_id)
    category_id = int(category_id)

    global record_id
    results = {}
    result_id = 0

    for record_id, record in records.items():
        if (record['User_id'] == user_id) or (record['Category_id'] == category_id):
            results[result_id] = {
                "Id": record['Id'],
                "User_id": record['User_id'],
                "Category_id": record['Category_id'],
                "Time": record['Time'],
                "Pay": record['Pay']
            }
            result_id += 1

    if not results:
        return "<p>Record not found</p>", 404
    
    return jsonify(results), 200