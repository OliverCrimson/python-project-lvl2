from gendiff.formatter import chose_formatter


def generate_diff(data1, data2, form):
    return chose_formatter(data1, data2, form)
