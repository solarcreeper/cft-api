def init_module(api):
    from app.api.disk.disk import disk
    api.add_namespace(disk)
