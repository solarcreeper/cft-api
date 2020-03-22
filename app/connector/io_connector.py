import re

from bson import ObjectId

from app.connector.base import to_dict
from app.data_model.io_model import IoModel, HisIoModel
from app import logger


class IoConnector(object):
    @classmethod
    def add(cls, **kwargs):
        io_name = kwargs['io_name']
        io_model = IoModel.objects(io_name=io_name).first()
        if io_model is None:
            if not kwargs.get('id'):
                kwargs['id'] = ObjectId()
            IoModel(**kwargs).save()
            return {'result': True, 'msg': 'OK'}
        else:
            logger.info("try to add io model failed, %s exist" % io_name)
            return {'result': False, 'msg': 'io name repeat'}

    @classmethod
    def delete(cls, **kwargs):
        args = {}
        delete_list = []
        if 'io_name' in kwargs:
            args['io_name'] = kwargs['io_name']
        io_model_list = list(IoModel.objects(**args))
        if len(io_model_list) == 0:
            logger.info("found 0 result for search condition: %s" % args)
        else:
            for record in io_model_list:
                logger.info("delete io model %s" % record.io_name)
                delete_list.append(to_dict(record))
                record.delete()
        return {'result': True, 'msg': 'deleted io model: %s' % delete_list}

    @classmethod
    def query(cls, **kwargs):
        page = int(kwargs.pop('page'))
        per_page = int(kwargs.pop('per_page'))

        args = {}
        for item in kwargs:
            args[item] = re.compile(kwargs[item])

        pagination = IoModel.objects(**args).paginate(page=page, per_page=per_page)
        result = {'result': True, 'msg': 'OK', 'page': pagination.page,
                  'total': pagination.total, 'per_page': pagination.per_page, 'data': []}
        for item in pagination.items:
            result['data'].append(to_dict(record=item, remove_id=True))
        return result


class HisIoConnector(object):
    @classmethod
    def add(cls, **kwargs):
        if not kwargs.get('id'):
            kwargs['id'] = ObjectId()
        HisIoModel(**kwargs).save()
        return {'result': True, 'msg': 'OK'}

    @classmethod
    def delete(cls, **kwargs):
        args = {}
        delete_list = []
        if 'io_name' in kwargs:
            args['io_name'] = kwargs['io_name']

        his_io_list = list(HisIoModel.objects(**args))
        if len(his_io_list) == 0:
            logger.info("found 0 result for search condition: %s" % args)
        else:
            for record in his_io_list:
                logger.info("delete io model %s" % record.io_name)
                delete_list.append(to_dict(record))
                record.delete()
        return {'result': True, 'msg': 'deleted io model: %s' % delete_list}

    @classmethod
    def query(cls, **kwargs):
        page = int(kwargs.pop('page'))
        per_page = int(kwargs.pop('per_page'))

        args = {}
        for item in kwargs:
            args[item] = re.compile(kwargs[item])

        pagination = HisIoModel.objects(**args).paginate(page=page, per_page=per_page)
        result = {'result': True, 'msg': 'OK', 'page': pagination.page,
                  'total': pagination.total, 'per_page': pagination.per_page, 'data': []}
        for item in pagination.items:
            result['data'].append(to_dict(record=item, remove_id=True))
        return result
