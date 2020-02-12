from bson import ObjectId

from app.data_model.user_model import UserModel
from config import logger


class UserConnector(object):
    @classmethod
    def query(cls, **kwargs):
        if 'username' in kwargs:
            return UserModel.objects(username=kwargs.get('username')).first()
        else:
            return list(UserModel.objects())

    @classmethod
    def update(cls, user_info, **kwargs):
        try:
            user_info.update(**kwargs)
            user_info.reload()
            return user_info
        except Exception as err:
            logger.info(err)

    @classmethod
    def delete(cls, username):
        UserModel.objects.get(username=username).delete()

    @classmethod
    def add(cls, **kwargs):
        user = UserModel.objects(username=kwargs.get('username')).first()
        if user is None:
            if not kwargs.get('id'):
                kwargs['id'] = ObjectId()
            user = UserModel(**kwargs).save()
        return user
