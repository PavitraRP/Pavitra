def MyPlexer(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper
