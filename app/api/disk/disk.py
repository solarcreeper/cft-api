from flask_restplus import Namespace, Resource
from app.api.disk import parameters as params
from flask_restplus import fields

from app.connector.disk_connector import DiskConnector

disk_api = Namespace('disk_info')

disk_model = disk_api.model('disk_model', {
    'id': fields.String(readOnly=True, description='id'),
    'ip_address': fields.String(readOnly=True, description='belonged device ip address, format{8.46.0.1}'),
    'type': fields.String(readOnly=True, description='disk type, format{SSD|SAS|NL_SAS}'),
    'capacity': fields.String(readOnly=True, description='disk capacity, format{xxxGB}'),
    'vender': fields.String(readOnly=True, description='disk manufacturer, format{WD|WEST}'),
    'number': fields.String(readOnly=True, description='same disks belonged to one device, format{xx}'),
    'date': fields.Date(readOnly=True, description='data collected date, format{2019-01-01}')
})


@disk_api.route('')
class DiskInfo(Resource):
    @disk_api.doc(parser=params.disk_query, description='query')
    @disk_api.marshal_list_with(disk_model)
    def get(self):
        disks = DiskConnector.query(**params.disk_query.parse_args())
        return disks

    @disk_api.doc(parser=params.disk_post, description='save')
    @disk_api.expect(disk_model)
    @disk_api.marshal_list_with(disk_model)
    def post(self):
        args = params.disk_post.parse_args()
        return DiskConnector.add(**args)

    @disk_api.doc(parser=params.disk_delete, description='delete')
    @disk_api.marshal_list_with(disk_model)
    def delete(self):
        name = params.disk_delete.parse_args()['name']
        books = DiskConnector.delete(name)
        return books
