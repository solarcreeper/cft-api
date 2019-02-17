from flask_restplus.reqparse import Argument

from app.api.reqparser import ReqParser

env_post = ReqParser()
env_post.add_arguments(
    Argument(name='env', required=True, help='env name, format{xxxxxx}'),
    Argument(name='type', required=True, help='env type, format{SSD|SAS|NL_SAS}'),
    Argument(name='capacity', required=True, help='env capacity, format{xxxGB}'),
    Argument(name='vender', required=True, help='env manufacturer, format{WD|WEST}'),
    Argument(name='number', required=True, help='same disks belonged to one device, format{xx}'),
    Argument(name='date', required=True, help='data collected date, format{2019-01-01}'))

env_query = ReqParser()
env_query.add_arguments(
    Argument(name='ip_address', required=False, help='belonged device ip address, format{8.46.0.1}'))

env_delete = ReqParser()
env_delete.add_arguments(
    Argument(name='ip_address', required=False, help='belonged device ip address, format{8.46.0.1}'))

env_update = ReqParser()
env_update.add_arguments(
    Argument(name='ip_address', required=False, help='belonged device ip address, format{8.46.0.1}'),
    Argument(name='type', required=False, help='env type, format{SSD|SAS|NL_SAS}'),
    Argument(name='capacity', required=False, help='env capacity, format{xxxGB}'),
    Argument(name='vender', required=False, help='env manufacturer, format{WD|WEST}'),
    Argument(name='number', required=False, help='same disks belonged to one device, format{xx}'),
    Argument(name='date', required=False, help='data collected date, format{2019-01-01}'))
