def init_module(api):
    from app.api.system_info.system_info import system_info_api
    api.add_namespace(system_info_api)
