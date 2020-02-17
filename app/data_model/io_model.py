from app.data_model import db


class IoModel(db.Document):
    io_name = db.StringField(required=True)
    tool_name = db.StringField(required=True)
    io_params = db.StringField(required=True)
