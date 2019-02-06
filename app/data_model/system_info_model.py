from app.data_model import db


class System_Info_Model(db.Document):
    device_sn = db.StringField(required=True)
    ip_address = db.StringField(required=True)
    device_model = db.StringField(required=True)
    version = db.StringField(required=True)
    date = db.StringField(required=True)
