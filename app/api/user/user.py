from flask_restplus import Namespace, Resource
from app.api.user import parameters as params
from flask_restplus import fields

from app.connector.user_connector import UserConnector

user_api = Namespace('user')

user_model = user_api.model('user_model', {
    'id': fields.String(readOnly=True, description='id'),
    'username': fields.String(readOnly=True, description='username'),
    'password': fields.String(readOnly=True, description='password'),
})


@user_api.route('')
class User(Resource):
    @user_api.doc(parser=params.get_user, description='query')
    @user_api.marshal_list_with(user_model)
    def get(self):
        args = params.get_user.parse_args()
        users = UserConnector.query(**args)
        return users

    @user_api.doc(parser=params.add_user, description='save')
    @user_api.expect(user_model)
    @user_api.marshal_list_with(user_model)
    def post(self):
        args = params.add_user.parse_args()
        return UserConnector.add(**args)

    @user_api.doc(parser=params.delete_user, description='delete')
    @user_api.marshal_list_with(user_model)
    def delete(self):
        args = params.add_user.parse_args()
        return UserConnector.delete(args['username'])