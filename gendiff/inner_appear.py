
def key_gathering(dict_one, dict_two):
    first_file = set(dict_one.keys())
    second_file = set(dict_two.keys())
    gathered_keys = sorted(first_file.union(second_file))
    print(gathered_keys)
    result = {}
    for key in gathered_keys:
        # calculate_diff(dict_one, dict_two, key)
        result[key] = calculate_diff(dict_one, dict_two, key)

    return result


# def calculate_diff(dict_one, dict_two, key):
# # dict