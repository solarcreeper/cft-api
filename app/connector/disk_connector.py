from bson import ObjectId

from app.data_model.disk_model import Disk_Model


class DiskConnector(object):
    @classmethod
    def query(cls, **kwargs):
        disk_info = Disk_Model.objects(ip_address=kwargs.get('ip_address')).first()
        return disk_info

    @classmethod
    def update(cls, disk_info, **kwargs):
        try:
            disk_info.update(**kwargs)
            disk_info = disk_info.reload()
            return disk_info
        except Exception as err:
            print(err)

    @classmethod
    def delete(cls, ip_address):
        Disk_Model.objects.get(ip_address=ip_address).delete()

    @classmethod
    def add(cls, **kwargs):
        disk_obj = Disk_Model.objects(device_sn=kwargs.get('device_sn')).first()
        if disk_obj is None:
            if not kwargs.get('id'):
                kwargs['id'] = ObjectId()
            disk_obj = Disk_Model(**kwargs).save()
        return disk_obj
