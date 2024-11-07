from . import db

class PocketModel(db.Model):
    __tablename__ = "pocket"

    Id = db.Column(db.Integer, primary_key = True)
    Money = db.Column(db.Integer)

    user = db.relationship("UserModel", back_populates="pocket", lazy="dynamic")

class UserModel(db.Model):
    __tablename__ = "user"

    Id = db.Column(db.Integer, primary_key = True)
    Pocket_id = db.Column(db.Integer, db.ForeignKey("pocket.Id"), nullable=False)
    Name = db.Column(db.String(128), unique=True, nullable=False)

    record = db.relationship("RecordModel", back_populates="user", lazy="dynamic")
    pocket = db.relationship("PocketModel", back_populates="user")

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