from app.data_model import db


class UserModel(db.Document):
    username = db.StringField(required=True)
    password = db.StringField(required=True)