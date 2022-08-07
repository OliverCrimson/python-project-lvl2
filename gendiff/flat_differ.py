import json
# import os


def json_to_python(file: str):
    with open(file, "r") as some_file:
        result = json.load(some_file)
    return result


def forming(item):
    str_from_dict = '\n'.join(
        [f'{key}: {str(value).lower()}'
            for key, value in item.items()])
    return str_from_dict


def generate_diff(one, two):
    first_file = list(one.keys())
    second_file = list(two.keys())
    key_list = []
    values_list = []
    gathered_keys = sorted(first_file + second_file)
    for item in gathered_keys:
        if one.get(item) == two.get(item):
            key_list.append('  ' + item)
            values_list.append(one.get(item))
        if item in first_file and item in second_file:
            if one.get(item) != two.get(item):
                key_list.append('- ' + item)
                key_list.append('+ ' + item)
                values_list.append(one.get(item))
                values_list.append(two.get(item))
        if item in second_file and item not in first_file:
            key_list.append('+ ' + item)
            values_list.append(two.get(item))
        if item in first_file and item not in second_file:
            key_list.append('- ' + item)
            values_list.append(one.get(item))
    dicted_result = dict(list(zip(key_list, values_list)))
    result = forming(dicted_result)
    return "{" + "\n" + result + "\n" + "}"
