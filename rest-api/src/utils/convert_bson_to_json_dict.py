from bson import ObjectId


def convert_bson_to_json_dict(bson_document: dict):
    """
    converts dictionary with BSON datatypes to json-serializable dict

    handles only `ObjectId` datatype
    """

    json_dict = dict(**bson_document)

    def stringify_object_ids(data: dict | list):
        if isinstance(data, list):
            data_as_dict = {index: value for (index, value) in enumerate(data)}
        else:
            data_as_dict = data

        for key in data_as_dict:
            value = data_as_dict[key]

            if isinstance(value, dict) or isinstance(value, list):
                stringify_object_ids(value)
            elif isinstance(value, ObjectId):
                data[key] = str(value)

    stringify_object_ids(json_dict)

    return json_dict
