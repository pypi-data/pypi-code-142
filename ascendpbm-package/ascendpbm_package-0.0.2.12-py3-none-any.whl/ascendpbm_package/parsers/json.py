
# recursive function to help flatten some of the responses
# can we do better than pandas here?
# It'd get rid of a lot of response-specific indexing...
def recursive_keys(dictio):
    keys = []
    for key, value in dictio.items():
        if isinstance(value, dict):
            keys.append(key)
            keys.append(recursive_keys(value))
        else:
            keys.append(key)
    return keys


