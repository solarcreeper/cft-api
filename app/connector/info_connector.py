from bson import ObjectId

from app.data_model.info_model import InfoModel


class InfoConnector(object):
    @classmethod
    def query(cls, **kwargs):
        system_info = InfoModel.objects(env_name=kwargs.get('env_name')).first()
        return system_info

    @classmethod
    def update(cls, **kwargs):
        try:
            system_info = InfoModel.objects(env_name=kwargs.get('env_name')).first()
            system_info.update(**kwargs)
            system_info = system_info.reload()
            return system_info
        except Exception as err:
            print(err)

    @classmethod
    def delete(cls, env_name):
        InfoModel.objects.get(env_name=env_name).delete()

    @classmethod
    def add(cls, **kwargs):
        system_info_obj = InfoModel.objects(env_name=kwargs.get('env_name')).first()
        if system_info_obj is None:
            if not kwargs.get('id'):
                kwargs['id'] = ObjectId()
            system_info_obj = InfoModel(**kwargs).save()
        return system_info_obj
