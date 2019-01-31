from flask_mongoengine import MongoEngine

db = MongoEngine()


def init_module(app):
    db.init_app(app)
