from flask_restplus import Namespace, Resource
from app.api.book import parameters as params
from app.connector.book_connector import BookController
from flask_restplus import fields

ns = Namespace('ns')

bookModule = ns.model('book_model', {
    'id': fields.String(readOnly=True, description='id'),
    'name': fields.String(readOnly=True, description='book_model name'),
    'author': fields.String(readOnly=True, description='book_model author')
})


@ns.route('')
class HelloWorld(Resource):
    @ns.doc(parser=params.book_query, description='query')
    @ns.marshal_list_with(bookModule)
    def get(self):
        books = BookController.query(**params.book_query.parse_args())
        return books

    @ns.doc(parser=params.book_post, description='save')
    @ns.expect(bookModule)
    @ns.marshal_list_with(bookModule)
    def post(self):
        args = params.book_post.parse_args()
        return BookController.add(**args)

    @ns.doc(parser=params.book_delete, description='delete')
    @ns.marshal_list_with(bookModule)
    def delete(self):
        name = params.book_delete.parse_args()['name']
        books = BookController.delete(name)
        return books
