from app.data_model import db


class EnvModel(db.Document):
    env_name = db.StringField(required=True)
    user = db.StringField(required=False)
    check_flag = db.StringField(required=True)
    date = db.StringField(required=True)
