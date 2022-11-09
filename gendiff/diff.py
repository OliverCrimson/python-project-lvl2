from gendiff.formatter import chose_formatter


def generate_diff(data1, data2, form='stylish'):
    return chose_formatter(data1, data2, form)
