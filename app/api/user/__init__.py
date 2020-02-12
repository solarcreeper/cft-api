def init_module(api):
    from app.api.user.user import user_api
    api.add_namespace(user_api)
