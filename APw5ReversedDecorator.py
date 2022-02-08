from functools import wraps


def reversed_dec(func):
    @wraps(func)
    def inner(*args, **kwargs):
        args = tuple(reversed(args))
        return func(*args, **kwargs)
    return inner
