__version__ = '0.3.0'


def extends(cls):
    """Add method to class.
    Method should have at least one argument which will be used as reference to object (i.e. self).
    :param cls: Class to which method should be added
    :return:
    """

    def decorator(func):
        setattr(cls, func.__name__, func)
        return func

    return decorator
