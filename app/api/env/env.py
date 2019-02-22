from flask_restplus import Namespace, Resource
from app.api.env import parameters as params
from flask_restplus import fields

from app.connector.env_connector import EnvConnector

env_api = Namespace('env_info')

env_model = env_api.model('env_model', {
    'id': fields.String,
    'env_name': fields.String,
    'user': fields.String,
    'check_flag': fields.String,
    'date': fields.String
})


@env_api.route('')
class EvnInfo(Resource):
    @env_api.doc(parser=params.env_query, description='query')
    @env_api.marshal_list_with(env_model)
    def get(self):
        env = EnvConnector.query(**params.env_query.parse_args())
        return env

    @env_api.doc(parser=params.env_post, description='save')
    @env_api.expect(env_model)
    @env_api.marshal_list_with(env_model)
    def post(self):
        args = params.env_post.parse_args()
        return EnvConnector.add(**args)

    @env_api.doc(parser=params.env_delete, description='delete')
    @env_api.marshal_list_with(env_model)
    def delete(self):
        name = params.env_delete.parse_args()['env_name']
        env = EnvConnector.delete(name)
        return env

    @env_api.doc(parser=params.env_post, description='update')
    @env_api.expect(env_model)
    @env_api.marshal_list_with(env_model)
    def put(self):
        args = params.env_post.parse_args()
        return EnvConnector.add(**args)
