from app.data_model import db


class IoModel(db.Document):
    io_name = db.StringField(required=True)
    tool_name = db.StringField(required=True)
    io_params = db.StringField(required=True)


class HisIoModel(db.Document):
    io_name = db.StringField(required=True, unique=True)
    tool_name = db.StringField(required=True)
    io_params = db.StringField(required=True)
    device_model = db.StringField(required=True)
    device_version = db.StringField(required=True)
    script_name = db.StringField(required=True)
    date = db.StringField(required=True)
    result = db.StringField(required=True)
