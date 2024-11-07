from . import db

class UserModel(db.Model):
    __tablename__ = "user"

    Id = db.Column(db.Integer, primary_key = True)
    Name = db.Column(db.String(128), unique=True, nullable=False)

    record = db.relationship("RecordModel", back_populates="user", lazy="dynamic")

class CategoryModel(db.Model):
    __tablename__ = "category"

    Id = db.Column(db.Integer, primary_key = True)
    Name = db.Column(db.String(128), unique=True, nullable=False)

    record = db.relationship("RecordModel", back_populates="category", lazy="dynamic")

class RecordModel(db.Model):
    __tablename__ = "record"

    Id = db.Column(db.Integer, primary_key = True)
    User_id = db.Column(db.Integer, db.ForeignKey("user.Id"), nullable=False)
    Category_id = db.Column(db.Integer, db.ForeignKey("category.Id"), nullable=False)
    Time = db.Column(db.String, nullable=False)
    Pay = db.Column(db.Integer, nullable=False)

    user = db.relationship("UserModel", back_populates="record")
    category = db.relationship("CategoryModel", back_populates="record")