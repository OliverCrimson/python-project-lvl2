from gendiff.defrag_kids import build
from gendiff.formatter import formatting
from gendiff.loader import get_data


def generate_diff(data1, data2, form='stylish'):
    built_appear = build(get_data(data1), get_data(data2))
    return formatting(built_appear, form)
