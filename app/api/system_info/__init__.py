def init_module(api):
    from app.api.system_info.system_info import monitor
    api.add_namespace(monitor)
