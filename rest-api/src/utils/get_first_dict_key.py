def get_first_dict_key(target: dict):
    keys = list(target)
    if len(keys) < 1:
        return None
    
    return keys[0]
