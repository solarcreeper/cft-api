def init_module(api):
    from app.api.book.resources import ns
    api.add_namespace(ns)
