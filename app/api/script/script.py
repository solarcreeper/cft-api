import json

from flask_restplus import Namespace, Resource
from app.api.script import parameters as params
from flask_restplus import fields

from app.connector.script_connector import ScriptConnector, HisScriptConnector

script_api = Namespace('script')

script_model = script_api.model('script_model', {
    'id': fields.String(readOnly=True, description='id'),
    'script_name': fields.String(readOnly=True, description='script name'),
    'script_path': fields.String(readOnly=True, description='script_path'),
    'script_params': fields.String(readOnly=True, description='script_params'),
    'classification': fields.String(readOnly=True, description='classification'),
    'script_desc': fields.String(readOnly=True, description='script_desc')
})

his_script_model = script_api.model('his_script_model', {
    'id': fields.String(readOnly=True, description='id'),
    'script_name': fields.String(readOnly=True, description='script name'),
    'script_path': fields.String(readOnly=True, description='script_path'),
    'script_params': fields.String(readOnly=True, description='script_params'),
    'classification': fields.String(readOnly=True, description='classification'),
    'script_desc': fields.String(readOnly=True, description='script_desc'),
    'device_model': fields.String(readOnly=True, description='running device model'),
    'device_version': fields.String(readOnly=True, description='running device version'),
    'date': fields.String(readOnly=True, description='date'),
    'result': fields.String(readOnly=True, description='result')
})


@script_api.route('')
class Script(Resource):
    @script_api.doc(parser=params.add_script, description='save')
    @script_api.expect(script_model)
    def post(self):
        args = params.add_script.parse_args()
        if 'script_params' in args:
            args['script_params'] = json.loads(args['script_params'])
        return ScriptConnector.add(**args)

    @script_api.doc(parser=params.delete_script, description='delete')
    def delete(self):
        args = params.delete_script.parse_args()
        return ScriptConnector.delete(**args)

    @script_api.doc(parser=params.get_script, description='query')
    def get(self):
        args = params.get_script.parse_args()
        return ScriptConnector.query(**args)


@script_api.route('/his_script')
class HisScript(Resource):
    @script_api.doc(parser=params.add_his_script, description='save')
    @script_api.expect(his_script_model)
    def post(self):
        args = params.add_his_script.parse_args()
        if 'script_params' in args:
            args['script_params'] = json.loads(args['script_params'])
        return HisScriptConnector.add(**args)

    @script_api.doc(parser=params.del_his_script, description='delete')
    def delete(self):
        args = params.del_his_script.parse_args()
        return HisScriptConnector.delete(**args)

    @script_api.doc(parser=params.get_his_script, description='query')
    def get(self):
        args = params.get_his_script.parse_args()
        return HisScriptConnector.query(**args)
