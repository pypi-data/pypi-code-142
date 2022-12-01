import sys


class MutuallyExclusiveArgsError(ValueError):
    ...


def mutex(*mutex_args: str):
    def wrapper(f):
        def inner(*args, **kwargs):
            validate(kwargs)
            return f(*args, **kwargs)

        def validate(kwargs: dict) -> None:
            mutex_args_w_provided_values = [v for k, v in kwargs if k in mutex_args and v is not None]
            if len(mutex_args_w_provided_values) != 1:
                raise MutuallyExclusiveArgsError("Mutually exclusive arguments can only have one value provided!")

        return inner

    return wrapper
