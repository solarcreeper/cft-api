from app.data_model import db


class Disk_Model(db.Document):
    ip_address = db.StringField(required=True)
    type = db.StringField(required=True)
    capacity = db.StringField(required=True)
    vender = db.StringField(required=True)
    number = db.StringField(required=True)
    date = db.StringField(required=True)
