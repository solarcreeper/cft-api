from flask_restplus import Namespace, Resource
from app.api.sys_info import parameters as params
from app.connector.info_connector import InfoConnector
from flask_restplus import fields

sys_info_api = Namespace('sys_info')

server_model = sys_info_api.model('server_model', {
    'ip': fields.String,
    'type': fields.String,
    'username': fields.String,
    'password': fields.String
})

version_model = sys_info_api.model('version_model', {
    'ver': fields.String,
    'sub': fields.String,
})

disk_model = sys_info_api.model('disk_model', {
    'type': fields.String,
    'capacity': fields.String,
    'manufacturer': fields.String,
    'model': fields.String,
    'manufacturer_capacity': fields.String,
})

interface_model = sys_info_api.model('interface_model', {
    'type': fields.String
})

cpu_model = sys_info_api.model('cpu_model', {
    'size': fields.String,
    'num': fields.String,
    'type': fields.String
})

mem_model = sys_info_api.model('mem_model', {
    'size': fields.String,
    'num': fields.String,
    'type': fields.String
})

storage_model = sys_info_api.model('storage_model', {
    "model": fields.String,
    "sn": fields.String,
    "controllers": fields.String,
    'ip': fields.List(fields.String),
    'version': fields.Nested(version_model),
    'disk': fields.List(fields.Nested(disk_model)),
    'interface': fields.List(fields.Nested(interface_model)),
    'cpu': fields.Nested(cpu_model),
    'mem': fields.Nested(mem_model)
})
system_info_model = sys_info_api.model('info_model', {
    'id': fields.String,
    'env_name': fields.String,
    'date': fields.Date,
    'server': fields.List(fields.Nested(server_model)),
    'storage': fields.List(fields.Nested(storage_model))
})


@sys_info_api.route('')
class SystemInfo(Resource):
    @sys_info_api.doc(parser=params.info_query, description='query')
    @sys_info_api.marshal_list_with(system_info_model)
    def get(self):
        system_info = InfoConnector.query(**params.info_query.parse_args())
        return system_info

    @sys_info_api.doc(parser=params.info_post, description='save')
    @sys_info_api.expect(system_info_model)
    @sys_info_api.marshal_list_with(system_info_model)
    def post(self):
        args = params.info_post.parse_args()
        return InfoConnector.add(**args)

    @sys_info_api.doc(parser=params.info_delete, description='delete')
    @sys_info_api.marshal_list_with(system_info_model)
    def delete(self):
        name = params.info_delete.parse_args()['name']
        books = InfoConnector.delete(name)
        return books
