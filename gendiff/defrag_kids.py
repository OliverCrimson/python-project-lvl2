def calculate_diff(dict_one, dict_two):
    nodes = []

    keys = dict_one.keys() | dict_two.keys()

    for key in sorted(keys):
        if key not in dict_two:
            nodes.append(dict(
                type_node='deleted',
                key=key,
                value=dict_one[key],
            ))
        elif key not in dict_one:
            nodes.append(dict(
                type_node='new',
                key=key,
                value=dict_two[key],
            ))
        elif isinstance(dict_one[key], dict) and isinstance(
                dict_two[key], dict
        ):
            nodes.append(dict(
                type_node='nested',
                key=key,
                children=calculate_diff(dict_one[key], dict_two[key]),
            ))
        elif key in dict_one and key in dict_two:
            if dict_one[key] == dict_two[key]:
                nodes.append(dict(
                    type_node='equal',
                    key=key,
                    value=dict_one[key],
                ))
            if dict_one[key] != dict_two[key]:
                nodes.append(dict(
                    type_node='changed',
                    key=key,
                    value1=dict_one[key],
                    value2=dict_two[key],
                ))
    return nodes


def build(dict_one, dict_two):
    return dict(
        type_node='root', children=calculate_diff(dict_one, dict_two)
    )
