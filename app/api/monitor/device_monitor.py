from flask_restplus import Namespace, Resource
from app.api.monitor import parameters as params
from app.connector.book_connector import BookController
from flask_restplus import fields

monitor = Namespace('monitor')

bookModule = monitor.model('book_model', {
    'id': fields.String(readOnly=True, description='id'),
    'name': fields.String(readOnly=True, description='book_model name'),
    'author': fields.String(readOnly=True, description='book_model author')
})


@monitor.route('')
class HelloWorld(Resource):
    @monitor.doc(parser=params.book_query, description='query')
    @monitor.marshal_list_with(bookModule)
    def get(self):
        books = BookController.query(**params.book_query.parse_args())
        return books

    @monitor.doc(parser=params.book_post, description='save')
    @monitor.expect(bookModule)
    @monitor.marshal_list_with(bookModule)
    def post(self):
        args = params.book_post.parse_args()
        return BookController.add(**args)

    @monitor.doc(parser=params.book_delete, description='delete')
    @monitor.marshal_list_with(bookModule)
    def delete(self):
        name = params.book_delete.parse_args()['name']
        books = BookController.delete(name)
        return books
