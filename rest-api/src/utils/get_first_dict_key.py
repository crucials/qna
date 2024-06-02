def get_first_dict_key(input_dict: dict):
    keys = list(input_dict)
    if len(keys) < 1:
        return None

    return keys[0]
