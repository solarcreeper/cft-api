from bson import ObjectId

from app.data_model.system_info_model import System_Info_Model


class SystemInfoConnector(object):
    @classmethod
    def query(cls, **kwargs):
        system_info = System_Info_Model.objects(device_sn=kwargs.get('device_sn')).first()
        return system_info

    @classmethod
    def update(cls, system_info, **kwargs):
        try:
            system_info.update(**kwargs)
            book = system_info.reload()
            return book
        except Exception as err:
            print(err)

    @classmethod
    def delete(cls, device_sn):
        System_Info_Model.objects.get(device_sn=device_sn).delete()

    @classmethod
    def add(cls, **kwargs):
        system_info_obj = System_Info_Model.objects(device_sn=kwargs.get('device_sn')).first()
        if system_info_obj is None:
            if not kwargs.get('id'):
                kwargs['id'] = ObjectId()
            system_info_obj = System_Info_Model(**kwargs).save()
        return system_info_obj
