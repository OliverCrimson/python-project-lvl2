from gendiff.defrag_kids import build
from gendiff.formatters.stylish import walk_stylish
from gendiff.loader import load_file
from gendiff.formatters.plain import plain_form
from gendiff.formatters.json_form import json_to_dict


def chose_formatter(file_one, file_two, form='stylish'):
    if form == 'stylish':
        return walk_stylish(build(
            load_file(file_one), load_file(file_two)
        ))
    if form == 'plain':
        return plain_form(build(
            load_file(file_one), load_file(file_two)
        ))
    if form == 'json':
        return json_to_dict(build(
            load_file(file_one), load_file(file_two)
        ))
    else:
        raise Exception(f"{form} format is not supported")
