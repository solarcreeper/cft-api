def to_dict(record, remove_id=False):
    result = dict(record.to_mongo())
    if remove_id:
        result.pop('_id')
    return result