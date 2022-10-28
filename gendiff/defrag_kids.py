
def key_gathering(dict_one, dict_two):
    first_file = set(dict_one.keys())
    second_file = set(dict_two.keys())
    gathered_keys = sorted(first_file.union(second_file))
    result = {}
    for key in gathered_keys:
        calculate_diff(dict_one, dict_two, key)
        result[key] = calculate_diff(dict_one, dict_two, key)

    return result


def calculate_diff(dict_one, dict_two, key):
    if key in dict_one and key in dict_two:
        if type(dict_one[key]) == dict and type(dict_two[key]) == dict:
            return {
                'status': 'got kids',
                'data': key_gathering(dict_one[key], dict_two[key])
            }

        if dict_one[key] == dict_two[key]:
            return {
                'status': 'equal',
                'data': dict_one[key]
            }

        if dict_one[key] != dict_two[key]:
            return {
                'status': 'different',
                'data1': dict_one[key],
                'data2': dict_two[key]
            }

    if key in dict_one and key not in dict_two:
        return {
            'status': 'deleted',
            'data': dict_one[key]
        }

    if key in dict_two and key not in dict_one:
        return {
            'status': 'new',
            'data': dict_two[key]
        }
