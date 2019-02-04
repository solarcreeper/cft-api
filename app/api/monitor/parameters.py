from flask_restplus.reqparse import Argument

from app.api.reqparser import ReqParser

book_post = ReqParser()

book_post.add_arguments(
    Argument(name='name', required=True, help='book_model name', location='form'),
    Argument(name='author', required=True, help='book_model author', location='form'))

book_query = ReqParser()
book_query.add_arguments(
    Argument(name='name', required=True, help='book_model name'))

book_delete = ReqParser()
book_delete.add_arguments(
    Argument(name='name', required=True, help='book_model name'))

book_update = ReqParser()
book_update.add_arguments(
    Argument(name='name', required=True, help='book_model name'),
    Argument(name='author', required=True, help='book_model author'))
