from flask_restplus import Namespace, Resource
from app.api.system_info import parameters as params
from app.connector.system_info_connector import SystemInfoConnector
from flask_restplus import fields

system_info_api = Namespace('system_info')

system_info_model = system_info_api.model('system_info_model', {
    'id': fields.String(readOnly=True, description='id'),
    'device_sn': fields.String(readOnly=True, description='device sn identification, format{xxx...xxx}'),
    'ip_address': fields.String(readOnly=True, description='belonged device ip address, format{8.46.0.1}'),
    'device_model': fields.String(readOnly=True, description='device model, format{2200V3|..|18800V5}'),
    'version': fields.String(readOnly=True, description='device version, format{V500R007C30}'),
    'date': fields.Date(readOnly=True, description='data collected date, format{2019-01-01}')
})


@system_info_api.route('')
class SystemInfo(Resource):
    @system_info_api.doc(parser=params.info_query, description='query')
    @system_info_api.marshal_list_with(system_info_model)
    def get(self):
        system_info = SystemInfoConnector.query(**params.info_query.parse_args())
        return system_info

    @system_info_api.doc(parser=params.info_post, description='save')
    @system_info_api.expect(system_info_model)
    @system_info_api.marshal_list_with(system_info_model)
    def post(self):
        args = params.info_post.parse_args()
        return SystemInfoConnector.add(**args)

    @system_info_api.doc(parser=params.info_delete, description='delete')
    @system_info_api.marshal_list_with(system_info_model)
    def delete(self):
        name = params.info_delete.parse_args()['name']
        books = SystemInfoConnector.delete(name)
        return books
