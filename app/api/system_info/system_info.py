from flask_restplus import Namespace, Resource
from app.api.system_info import parameters as params
from app.connector.book_connector import BookController
from flask_restplus import fields

monitor = Namespace('system_info')

system_info_model = monitor.model('book_model', {
    'id': fields.String(readOnly=True, description='id'),
    'device_sn': fields.String(readOnly=True, description='device sn identification, format{xxx...xxx}'),
    'ip_address': fields.String(readOnly=True, description='belonged device ip address, format{8.46.0.1}'),
    'device_model': fields.String(readOnly=True, description='device model, format{2200V3|..|18800V5}'),
    'version': fields.String(readOnly=True, description='device version, format{V500R007C30}'),
    'date': fields.Date(readOnly=True, description='data collected date, format{2019-01-01}')
})


@monitor.route('')
class HelloWorld(Resource):
    @monitor.doc(parser=params.book_query, description='query')
    @monitor.marshal_list_with(system_info_model)
    def get(self):
        books = BookController.query(**params.book_query.parse_args())
        return books

    @monitor.doc(parser=params.book_post, description='save')
    @monitor.expect(system_info_model)
    @monitor.marshal_list_with(system_info_model)
    def post(self):
        args = params.book_post.parse_args()
        return BookController.add(**args)

    @monitor.doc(parser=params.book_delete, description='delete')
    @monitor.marshal_list_with(system_info_model)
    def delete(self):
        name = params.book_delete.parse_args()['name']
        books = BookController.delete(name)
        return books
