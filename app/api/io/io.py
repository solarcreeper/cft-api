from flask_restplus import Namespace, Resource
from app.api.io import parameters as params
from flask_restplus import fields

from app.connector.io_connector import IoConnector

io_api = Namespace('io')

io_model = io_api.model('io_model', {
    'id': fields.String(readOnly=True, description='id'),
    'io_name': fields.String(readOnly=True, description='username'),
    'io_tool': fields.String(readOnly=True, description='password'),
    'io_params': fields.String(readOnly=True, description='password'),
})


@io_api.route('')
class IO(Resource):
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



