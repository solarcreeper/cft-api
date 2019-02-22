import os
from importlib import import_module

from flask import Blueprint
from flask_restplus import Api
from setuptools import find_packages

import config

api_bp = Blueprint(name='api', import_name=__name__, url_prefix='/%s/api/v1' % config.Config.APP_NAME)
api = Api(api_bp, version='1.0', title='SYSTEM MONITOR API', description='this is a demo for storage system sys_info')


def init_module(app):
    app.register_blueprint(api_bp)
    for module_name in find_packages(os.path.dirname(__file__)):
        module = import_module(name='.%s' % module_name, package=__name__)
        if hasattr(module, 'init_module'):
            module.init_module(api)
