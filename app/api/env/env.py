from flask_restplus import Namespace, Resource
from app.api.env import parameters as params
from flask_restplus import fields

from app.connector.disk_connector import DiskConnector

env_api = Namespace('disk_info')

disk_model = env_api.model('disk_model', {
    'id': fields.String(readOnly=True, description='id'),
    'env': fields.String(readOnly=True, description='env name, format{xxxxxx}'),
    'check_flag': fields.String(readOnly=True, description='env info check flag, format{True|Flase}')
})


@env_api.route('')
class EvnInfo(Resource):
    @env_api.doc(parser=params.disk_query, description='query')
    @env_api.marshal_list_with(disk_model)
    def get(self):
        disks = DiskConnector.query(**params.disk_query.parse_args())
        return disks

    @env_api.doc(parser=params.disk_post, description='save')
    @env_api.expect(disk_model)
    @env_api.marshal_list_with(disk_model)
    def post(self):
        args = params.disk_post.parse_args()
        return DiskConnector.add(**args)

    @env_api.doc(parser=params.disk_delete, description='delete')
    @env_api.marshal_list_with(disk_model)
    def delete(self):
        name = params.disk_delete.parse_args()['name']
        books = DiskConnector.delete(name)
        return books
