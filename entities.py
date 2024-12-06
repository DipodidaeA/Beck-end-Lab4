from marshmallow import Schema, fields

class PocketSchema(Schema):
    Id = fields.Int(required=True)
    Money = fields.Int(required=True)

class UserSchema(Schema):
    Id = fields.Int(required=True)
    Pocket_id = fields.Int(required=True)
    Name = fields.Str(required=True)
    Password = fields.Str(required=True)

class CategorySchema(Schema):
    Id = fields.Int(required=True)
    Name = fields.Str(required=True)

class RecordSchema(Schema):
    Id = fields.Int(required=True)
    User_id = fields.Int(required=True)
    Category_id = fields.Int(required=True)
    Time = fields.Str(required=True)
    Pay = fields.Int(required=True)