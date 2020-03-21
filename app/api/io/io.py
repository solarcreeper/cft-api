from flask_restplus import Namespace, Resource
from app.api.io import parameters as params
from flask_restplus import fields

from app.connector.io_connector import IoConnector, HisIoConnector

io_api = Namespace('io')

io_model = io_api.model('io_model', {
    'id': fields.String(readOnly=True, description='id'),
    'io_name': fields.String(readOnly=True, description='username'),
    'io_tool': fields.String(readOnly=True, description='password'),
    'io_params': fields.String(readOnly=True, description='password'),
})

his_io_model = io_api.model('his_io_model', {
    'id': fields.String(readOnly=True, description='id'),
    'io_name': fields.String(readOnly=True, description='username'),
    'io_tool': fields.String(readOnly=True, description='password'),
    'io_params': fields.String(readOnly=True, description='password'),
    'device_model': fields.String(readOnly=True, description='running device model'),
    'device_version': fields.String(readOnly=True, description='running device version'),
    'script_name': fields.String(readOnly=True, description='running script name'),
    'date': fields.String(readOnly=True, description='date'),
    'result': fields.String(readOnly=True, description='result')
})


@io_api.route('')
class Io(Resource):
    @io_api.doc(parser=params.add_io, description='save')
    @io_api.expect(io_model)
    def post(self):
        args = params.add_io.parse_args()
        return IoConnector.add(**args)

    @io_api.doc(parser=params.delete_io, description='delete')
    def delete(self):
        args = params.delete_io.parse_args()
        return IoConnector.delete(**args)

    @io_api.doc(parser=params.get_io, description='query')
    def get(self):
        args = params.get_io.parse_args()
        return IoConnector.query(**args)


@io_api.route('/his_io')
class HisIo(Resource):
    @io_api.doc(parser=params.add_his_io, description='save')
    @io_api.expect(his_io_model)
    def post(self):
        args = params.add_his_io.parse_args()
        return HisIoConnector.add(**args)

    @io_api.doc(parser=params.del_his_io, description='delete')
    def delete(self):
        args = params.del_his_io.parse_args()
        return HisIoConnector.delete(**args)

    @io_api.doc(parser=params.get_his_io, description='query')
    def get(self):
        args = params.get_his_io.parse_args()
        return HisIoConnector.query(**args)
