from bson import ObjectId

from app.data_model.env_model import EnvModel


class EnvConnector(object):
    @classmethod
    def query(cls, **kwargs):
        env_info = EnvModel.objects(env_name=kwargs.get('env_name')).first()
        return env_info

    @classmethod
    def update(cls, env_info, **kwargs):
        try:
            env_info.update(**kwargs)
            env_info = env_info.reload()
            return env_info
        except Exception as err:
            print(err)

    @classmethod
    def delete(cls, env_name):
        EnvModel.objects.get(env_name=env_name).delete()

    @classmethod
    def add(cls, **kwargs):
        env = EnvModel.objects(env_name=kwargs.get('env_name')).first()
        if env is None:
            if not kwargs.get('id'):
                kwargs['id'] = ObjectId()
                env = EnvModel  (**kwargs).save()
        return env
