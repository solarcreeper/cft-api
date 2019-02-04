from flask_restplus import Namespace, Resource
from app.api.disk import parameters as params
from flask_restplus import fields

from app.connector.book_connector import BookController

disk = Namespace('disk')

disk_module = disk.model('disk_model', {
    'id': fields.String(readOnly=True, description='id'),
    'ip_address': fields.String(readOnly=True, description='belonged device ip address, format{8.46.0.1}'),
    'type': fields.String(readOnly=True, description='disk type, format{SSD|SAS|NL_SAS}'),
    'capacity': fields.String(readOnly=True, description='disk capacity, format{xxxGB}'),
    'vender': fields.String(readOnly=True, description='disk manufacturer, format{WD|WEST}'),
    'number': fields.Integer(readOnly=True, description='same disks belonged to one device, format{xx}'),
    'date': fields.Date(readOnly=True, description='data collected date, format{2019-01-01}'),
})


@disk.route('')
class Disk(Resource):
    # @ns.doc 来标记这个 api 的作用
    @disk.doc(parser=params.book_query, description='query')
    # @ns.marshal_with来标记如何渲染返回的json
    @disk.marshal_list_with(disk_module)
    def get(self):
        books = BookController.query(**params.book_query.parse_args())
        return books

    @disk.doc(parser=params.book_post, description='save')
    @disk.expect(disk_module)
    @disk.marshal_list_with(disk_module)
    def post(self):
        args = params.book_post.parse_args()
        return BookController.add(**args)

    @disk.doc(parser=params.book_delete, description='delete')
    @disk.marshal_list_with(disk_module)
    def delete(self):
        name = params.book_delete.parse_args()['name']
        books = BookController.delete(name)
        return books
