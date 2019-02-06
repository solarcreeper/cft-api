from flask_restplus.reqparse import Argument

from app.api.reqparser import ReqParser

disk_post = ReqParser()
disk_post.add_arguments(
    Argument(name='ip_address', required=True, help='belonged device ip address, format{8.46.0.1}'),
    Argument(name='type', required=True, help='disk type, format{SSD|SAS|NL_SAS}'),
    Argument(name='capacity', required=True, help='disk capacity, format{xxxGB}'),
    Argument(name='vender', required=True, help='disk manufacturer, format{WD|WEST}'),
    Argument(name='number', required=True, help='same disks belonged to one device, format{xx}'),
    Argument(name='date', required=True, help='data collected date, format{2019-01-01}'))

disk_query = ReqParser()
disk_query.add_arguments(
    Argument(name='ip_address', required=False, help='belonged device ip address, format{8.46.0.1}'))

disk_delete = ReqParser()
disk_delete.add_arguments(
    Argument(name='ip_address', required=False, help='belonged device ip address, format{8.46.0.1}'))

disk_update = ReqParser()
disk_update.add_arguments(
    Argument(name='ip_address', required=False, help='belonged device ip address, format{8.46.0.1}'),
    Argument(name='type', required=False, help='disk type, format{SSD|SAS|NL_SAS}'),
    Argument(name='capacity', required=False, help='disk capacity, format{xxxGB}'),
    Argument(name='vender', required=False, help='disk manufacturer, format{WD|WEST}'),
    Argument(name='number', required=False, help='same disks belonged to one device, format{xx}'),
    Argument(name='date', required=False, help='data collected date, format{2019-01-01}'))
