from marshmallow import Schema, fields

class PlainUserSchema(Schema):
    Id = fields.Int(required=True)
    Name = fields.Str(required=True)

class PlainCategorySchema(Schema):
    Id = fields.Int(required=True)
    Name = fields.Str(required=True)

class PlainRecordSchema(Schema):
    Id = fields.Int(required=True)
    User_id = fields.Int(required=True)
    Category_id = fields.Int(required=True)
    Time = fields.Str(required=True)
    Pay = fields.Int(required=True)