def exception_logger(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as ex:
            if isinstance(ex, ZeroDivisionError):
                print('ZeroDivisionError')
            elif isinstance(ex, AssertionError):
                print('AssertionError')
            elif isinstance(ex, ArithmeticError):
                print('ArithmeticError')
            else:
                raise ex

    return inner
