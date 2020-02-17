from app.data_model import db


class IOLogModel(db.Document):
    io_name = db.StringField(required=True, unique=True)
    io_tool = db.StringField(required=True)
    io_params = db.StringField(required=True)
    running_device_model = db.StringField(required=True)
    running_device_version = db.StringField(required=True)
    running_date = db.DateTimeField(required=True)
    running_script_name = db.StringField()
    comment = db.StringField()
