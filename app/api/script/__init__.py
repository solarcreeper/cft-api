def init_module(api):
    from app.api.script.script import script_api
    api.add_namespace(script_api)
