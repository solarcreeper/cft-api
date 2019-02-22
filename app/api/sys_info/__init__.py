def init_module(api):
    from app.api.sys_info.sys_info import sys_info_api
    api.add_namespace(sys_info_api)
