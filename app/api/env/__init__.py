def init_module(api):
    from app.api.env.env import env_api
    api.add_namespace(env_api)
