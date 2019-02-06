from flask_restplus.reqparse import Argument

from app.api.reqparser import ReqParser

info_post = ReqParser()
info_post.add_arguments(
    Argument(name='device_sn', required=True, help='device sn identification, format{xxx...xxx}'),
    Argument(name='ip_address', required=True, help='belonged device ip address, format{8.46.0.1}'),
    Argument(name='device_model', required=True, help='device model, format{2200V3|..|18800V5}'),
    Argument(name='version', required=True, help='device version, format{V500R007C30}'),
    Argument(name='date', required=True, help='data collected date, format{2019-01-01}'))

info_query = ReqParser()
info_query.add_arguments(
    Argument(name='device_sn', required=False, help='device sn identification, format{xxx...xxx}'),
    Argument(name='ip_address', required=False, help='belonged device ip address, format{8.46.0.1}'))

info_delete = ReqParser()
info_delete.add_arguments(
    Argument(name='device_sn', required=False, help='device sn identification, format{xxx...xxx}'),
    Argument(name='ip_address', required=False, help='belonged device ip address, format{8.46.0.1}'))

info_update = ReqParser()
info_update.add_arguments(
    Argument(name='device_sn', required=False, help='device sn identification, format{xxx...xxx}'),
    Argument(name='ip_address', required=False, help='belonged device ip address, format{8.46.0.1}'),
    Argument(name='device_model', required=False, help='device model, format{2200V3|..|18800V5}'),
    Argument(name='version', required=False, help='device version, format{V500R007C30}'),
    Argument(name='date', required=False, help='data collected date, format{2019-01-01}'))
