import re

from bson import ObjectId

from app.connector.base import to_dict
from app.data_model.script_model import ScriptModel, HisScriptModel
from config import logger


class ScriptConnector(object):
    @classmethod
    def add(cls, **kwargs):
        script_name = kwargs['script_name']
        script_model = ScriptModel.objects(script_name=script_name).first()
        if script_model is None:
            if not kwargs.get('id'):
                kwargs['id'] = ObjectId()
            ScriptModel(**kwargs).save()
            return {'result': True, 'msg': 'OK'}
        else:
            logger.info("try to add script failed, %s exist" % script_name)
            return {'result': False, 'msg': 'io name repeat'}

    @classmethod
    def delete(cls, **kwargs):
        args = {}
        delete_list = []
        if 'script_name' in kwargs:
            args['script_name'] = kwargs['script_name']
        script_model_list = list(ScriptModel.objects(**args))
        if len(script_model_list) == 0:
            logger.info("found 0 result for search condition: %s" % args)
        else:
            for record in script_model_list:
                logger.info("delete model %s" % record.script_name)
                delete_list.append(to_dict(record))
                record.delete()
        return {'result': True, 'msg': 'deleted model: %s' % delete_list}

    @classmethod
    def query(cls, **kwargs):
        page = int(kwargs.pop('page'))
        per_page = int(kwargs.pop('per_page'))

        args = {}
        for item in kwargs:
            args[item] = re.compile(kwargs[item])

        pagination = ScriptModel.objects(**args).paginate(page=page, per_page=per_page)
        result = {'result': True, 'msg': 'OK', 'page': pagination.page,
                  'total': pagination.total, 'per_page': pagination.per_page, 'data': []}
        for item in pagination.items:
            result['data'].append(to_dict(record=item, remove_id=True))
        return result


class HisScriptConnector(object):
    @classmethod
    def add(cls, **kwargs):
        if not kwargs.get('id'):
            kwargs['id'] = ObjectId()
        HisScriptModel(**kwargs).save()
        return {'result': True, 'msg': 'OK'}

    @classmethod
    def delete(cls, **kwargs):
        args = {}
        delete_list = []
        if 'script_name' in kwargs:
            args['script_name'] = kwargs['script_name']

        his_script_list = list(HisScriptModel.objects(**args))
        if len(his_script_list) == 0:
            logger.info("found 0 result for search condition: %s" % args)
        else:
            for record in his_script_list:
                logger.info("delete model %s" % record.io_name)
                delete_list.append(to_dict(record))
                record.delete()
        return {'result': True, 'msg': 'deleted model: %s' % delete_list}

    @classmethod
    def query(cls, **kwargs):
        page = int(kwargs.pop('page'))
        per_page = int(kwargs.pop('per_page'))

        args = {}
        for item in kwargs:
            args[item] = re.compile(kwargs[item])

        pagination = HisScriptModel.objects(**args).paginate(page=page, per_page=per_page)
        result = {'result': True, 'msg': 'OK', 'page': pagination.page,
                  'total': pagination.total, 'per_page': pagination.per_page, 'data': []}
        for item in pagination.items:
            result['data'].append(to_dict(record=item, remove_id=True))
        return result
