def get_val(data, key, default='git'):
    if key in data:
        return data[key]
    else:
        return default
