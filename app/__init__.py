import os
import pkgutil
from importlib import import_module
from flask import Flask
from config import config
from flask_cors import CORS

def __init_module(app):
    for importer, module_name, ispkg in pkgutil.iter_modules([os.path.dirname(__file__)]):
        if ispkg:
            mod = import_module(name='.%s' % module_name, package=__name__)
            if hasattr(mod, 'init_module'):
                mod.init_module(app)


def create_app(config_mode):
    app = Flask(__name__)
    CORS(app, supports_credentials=True)
    # from_object 只有大写名称的值才会被存储到配置对象中，确保在配置键中使用大写字母
    app.config.from_object(config[config_mode])
    __init_module(app)
    return app
