def init_module(api):
    from app.api.disk.disk import disk_api
    api.add_namespace(disk_api)
