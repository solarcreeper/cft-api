from app.data_model import db


class Book(db.Document):
    name = db.StringField(required=True)
    author = db.StringField(required=True)
