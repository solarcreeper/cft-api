def init_module(api):
    from app.api.io.io import io_api
    api.add_namespace(io_api)
