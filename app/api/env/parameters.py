from flask_restplus.reqparse import Argument

from app.api.reqparser import ReqParser

env_post = ReqParser()
env_post.add_arguments(
    Argument(name='env_name', required=True, help='env name, format{xxxxxx}'),
    Argument(name='env_usage', required=True, help='env name, format{xxxxxx}'),
    Argument(name='user', required=True, help='env user, format{xxx}'),
    Argument(name='check_flag', required=True, help='env check, format{xx}'),
    Argument(name='date', required=True, help='data collected date, format{2019-01-01}'))

env_query = ReqParser()
env_query.add_arguments(
    Argument(name='env_name', required=True, help='env name, format{xxxxxx}'))

env_delete = ReqParser()
env_delete.add_arguments(
    Argument(name='env_name', required=True, help='env name, format{xxxxxx}'))

env_update = ReqParser()
env_update.add_arguments(
    Argument(name='env_name', required=True, help='env name, format{xxxxxx}'),
    Argument(name='env_usage', required=True, help='env name, format{xxxxxx}'),
    Argument(name='user', required=True, help='env user, format{xxx}'),
    Argument(name='check_flag', required=True, help='env check, format{xx}'),
    Argument(name='date', required=True, help='data collected date, format{2019-01-01}'))