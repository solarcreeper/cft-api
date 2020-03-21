def init_module(api):
    from app.api.strategy.strategy import strategy_api
    api.add_namespace(strategy_api)
