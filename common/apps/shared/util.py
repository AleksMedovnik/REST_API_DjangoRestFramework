def get_exclude_query(request_get):
    exclude_query = {}
    for key in request_get:
        if key[-3:] == '_ne':
            exclude_query.update({key[:-3]: request_get[key]})
    return exclude_query