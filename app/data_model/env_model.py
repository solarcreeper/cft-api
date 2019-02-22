import mongoengine


class EnvModel(mongoengine.Document):
    env_name = mongoengine.StringField(required=True)
    env_usage = mongoengine.StringField(required=True)
    user = mongoengine.StringField(required=False)
    check_flag = mongoengine.StringField(required=True)
    date = mongoengine.StringField(required=True)
