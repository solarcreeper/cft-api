from app.data_model import db


class ParamsModel(db.EmbeddedDocument):
    param_key = db.StringField(required=True)
    param_value = db.StringField(required=True)


class ScriptModel(db.Document):
    script_name = db.StringField(required=True)
    script_path = db.StringField(required=True)
    script_params = db.EmbeddedDocumentListField(ParamsModel, required=False)
    classification = db.StringField(required=True)
    script_desc = db.StringField(required=True)


class HisScriptModel(db.Document):
    script_name = db.StringField(required=True)
    script_path = db.StringField(required=True)
    classification = db.StringField(required=True)
    script_desc = db.StringField(required=True)
    device_model = db.StringField(required=True)
    device_version = db.StringField(required=True)
    date = db.StringField(required=True)
    result = db.StringField(required=True)
