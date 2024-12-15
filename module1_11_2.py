import sys

def introspection_info(obj):
    info = {}
    info['type'] = type(obj).__name__
    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr))]
    info['attributes'] = attributes
    methods = [method for method in dir(obj) if callable(getattr(obj, method))]
    info['methods'] = methods

    return info

number_info = introspection_info(42)
print(number_info)