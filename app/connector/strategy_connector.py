import re

from bson import ObjectId

from app.connector.base import to_dict
from app.data_model.strategy_model import StrategyModel
from config import logger


class StrategyConnector(object):
    @classmethod
    def add(cls, **kwargs):
        strategy_name = kwargs['strategy_name']
        strategy_model = StrategyModel.objects(strategy_name=strategy_name).first()
        if strategy_model is None:
            if not kwargs.get('id'):
                kwargs['id'] = ObjectId()
            StrategyModel(**kwargs).save()
            return {'result': True, 'msg': 'OK'}
        else:
            logger.info("try to add model failed, %s exist" % strategy_name)
            return {'result': False, 'msg': 'io name repeat'}

    @classmethod
    def delete(cls, **kwargs):
        args = {}
        delete_list = []
        if 'strategy_name' in kwargs:
            args['strategy_name'] = kwargs['strategy_name']
        strategy_model_list = list(StrategyModel.objects(**args))
        if len(strategy_model_list) == 0:
            logger.info("found 0 result for search condition: %s" % args)
        else:
            for record in strategy_model_list:
                logger.info("delete model %s" % record.strategy_name)
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

        pagination = StrategyModel.objects(**args).paginate(page=page, per_page=per_page)
        result = {'result': True, 'msg': 'OK', 'page': pagination.page,
                  'total': pagination.total, 'per_page': pagination.per_page, 'data': []}
        for item in pagination.items:
            result['data'].append(to_dict(record=item, remove_id=True))
        return result
