def tree_walk(some, depth=0):
    string = '{\n'
    options = {
        'gap': '  ' * depth,
        'positive': '  + ',
        'negative': '  - ',
        'double': '    '
    }
    spare = options['gap'] * (depth - 1)
    for keys, values in some.items():
        if values['status'] == 'got kids':
            string += f'{options["gap"]}{options["double"]}{keys}: '\
                      f'{tree_walk(values["data"], depth + 2)}\n'
        if values['status'] == 'deleted':
            string += f'{options["gap"]}{options["negative"]}{keys}: '\
                      f'{stringify(values["data"], spare)}\n'
        if values['status'] == 'new':
            string += f'{options["gap"]}{options["positive"]}{keys}: '\
                      f'{stringify(values["data"], spare)}\n'
        if values['status'] == 'different':
            string += f'{options["gap"]}{options["negative"]}{keys}: '\
                      f'{stringify(values["data1"], spare)}\n'
            string += f'{options["gap"]}{options["positive"]}{keys}: '\
                      f'{stringify(values["data2"], spare)}\n'
        if values['status'] == 'equal':
            string += f'{options["gap"]}{options["double"]}{keys}: '\
                      f'{stringify(values["data"], spare)}\n'
    string += options["gap"] + '}'
    return string


def stringify(value, replacer='', depth=1):
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    if isinstance(value, dict):
        string = '{\n'
        gap = 2 * '  '
        new_indent = replacer + gap * (depth + 1)
        for key, val in value.items():
            string += f'{new_indent}{key}: '\
                      f'{stringify(val, replacer, depth + 1)}\n'
        backdoor = replacer + gap * depth
        string += backdoor + '}'
        return string
    return str(value)
