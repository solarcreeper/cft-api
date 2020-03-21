from app.data_model import db


class StrategyModel(db.Document):
    strategy_name = db.StringField(required=True)
    owner = db.StringField(required=True)
    io_list = db.ListField(required=False)
    script_list = db.ListField(required=False)
    fault_list = db.ListField(required=False)

