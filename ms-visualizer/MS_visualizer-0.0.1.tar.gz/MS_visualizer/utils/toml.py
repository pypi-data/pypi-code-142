import toml


def read_toml(path_or_filelike):
    try:
        with open(path_or_filelike) as f:
            toml_str = f.read()
    except TypeError:
        toml_str = path_or_filelike.read()
    return toml.loads(toml_str)