from importlib import import_module

_redis_client = None


def set_redis_client(class_path, **kwargs):
    global _redis_client
    module_name, class_name = class_path.rsplit('.', 1)
    client_class = getattr(import_module(module_name), class_name)
    _redis_client = client_class(**kwargs)


def get_redis_client():
    return _redis_client
