def init_module(api):
    from app.api.monitor.device_monitor import monitor
    api.add_namespace(monitor)
