# Create a MEGA decorator
def combine(*fns):
    def auth_fn(fn):
        for dec in reversed(fns):
            fn = dec(fn)
        return fn
    return auth_fn
