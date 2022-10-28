from gendiff.defrag_kids import key_gathering
from gendiff.formatters.stylish import tree_walk
from gendiff.loader import load_file
from gendiff.formatters.plain import plain_form
from gendiff.formatters.json_form import json_to_dict


def generate_diff(data1, data2, form='stylish'):
    if form == 'stylish':
        result = key_gathering(load_file(data1), load_file(data2))
        return tree_walk(result)
    if form == 'plain':
        result = key_gathering(load_file(data1), load_file(data2))
        return plain_form(result)
    if form == 'json':
        result = key_gathering(load_file(data1), load_file(data2))
        return json_to_dict(result)
