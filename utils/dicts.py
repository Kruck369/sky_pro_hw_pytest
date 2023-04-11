def get_val(collection, key, default='git'):
    if len(collection) == 0:
        value = default
    else:
        value = collection[key]
    return value
