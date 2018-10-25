from flask import Blueprint
from flask_restful import Api, Resource

from app.api.views import HelloWorld

api_bp = Blueprint('api', __name__)  # 这里的main只是为蓝本取得一个名字，并不一定要和main这个主程序包一致

api = Api(api_bp)

api.add_resource(HelloWorld, '/1')
