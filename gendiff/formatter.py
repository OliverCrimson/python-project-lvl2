from gendiff.formatters.stylish import walk_stylish
from gendiff.formatters.plain import plain_form
from gendiff.formatters.json_form import json_to_dict


def formatting(inner_appearance, form='stylish'):
    if form == 'stylish':
        return walk_stylish(inner_appearance)
    elif form == 'plain':
        return plain_form(inner_appearance)
    elif form == 'json':
        return json_to_dict(inner_appearance)
    else:
        raise Exception(f"{form} format is not supported")
