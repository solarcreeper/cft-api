import json

from flask_restplus import Namespace, Resource
from app.api.strategy import parameters as params
from flask_restplus import fields

from app.connector.strategy_connector import StrategyConnector

strategy_api = Namespace('strategy')

strategy_model = strategy_api.model('io_model', {
    'id': fields.String(readOnly=True, description='id'),
    'strategy_name': fields.String(readOnly=True, description='username'),
    'owner': fields.String(readOnly=True, description='password'),
    'io_list': fields.String(readOnly=True, description='password'),
    'script_list': fields.String(readOnly=True, description='password'),
    'fault_list': fields.String(readOnly=True, description='password'),
})


@strategy_api.route('')
class Strategy(Resource):
    @strategy_api.doc(parser=params.add_strategy, description='save')
    @strategy_api.expect(strategy_model)
    def post(self):
        args = params.add_strategy.parse_args()
        if 'io_list' in args:
            args['io_list'] = json.loads(args['io_list'])
        if 'script_list' in args:
            args['script_list'] = json.loads(args['script_list'])
        if 'fault_list' in args:
            args['fault_list'] = json.loads(args['fault_list'])
        return StrategyConnector.add(**args)

    @strategy_api.doc(parser=params.delete_strategy, description='delete')
    def delete(self):
        args = params.delete_strategy.parse_args()
        return StrategyConnector.delete(**args)

    @strategy_api.doc(parser=params.get_strategy, description='query')
    def get(self):
        args = params.get_strategy.parse_args()
        return StrategyConnector.query(**args)
