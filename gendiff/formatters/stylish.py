def stringify_v2(val, depth=0):
    if isinstance(val, dict):
        gap = ' ' * (depth * 4 - 2)
        lst = []
        new_line_spaces = gap + (' ' * 6)
        for keys, values in val.items():
            lst.append(f'{new_line_spaces}{keys}: '
                       f'{stringify_v2(values, depth + 1)}')
        outcome = '\n'.join(lst)
        return f'{{\n{outcome}\n  {gap}}}'
    if isinstance(val, bool):
        return str(val).lower()
    if val is None:
        return 'null'
    return str(val)


def walk_stylish(item, depth=0):
    children = item.get('children')
    options = {
        'gap': ' ' * (depth * 4 - 2),
        'positive': '+ ',
        'negative': '- ',
        'double': '  '
    }

    if item.get('type_node') == 'root':
        lst = map(lambda x: walk_stylish(x, depth + 1), children)
        outcome = '\n'.join(lst)
        return f'{{\n{outcome}\n}}'
    if item.get('type_node') == 'nested':
        lst = map(lambda x: walk_stylish(x, depth + 1), children)
        outcome = '\n'.join(lst)
        return f'{options["gap"]}{options["double"]}{item.get("key")}: ' \
               f'{{\n{outcome}\n  {options["gap"]}}}'
    if item.get('type_node') == 'new':
        return f'{options["gap"]}{options["positive"]}{item.get("key")}: ' \
               f'{stringify_v2(item.get("value"), depth)}'
    if item.get('type_node') == 'deleted':
        return f'{options["gap"]}{options["negative"]}{item.get("key")}: ' \
               f'{stringify_v2(item.get("value"), depth)}'
    if item.get('type_node') == 'equal':
        return f'{options["gap"]}{options["double"]}{item.get("key")}: ' \
               f'{stringify_v2(item.get("value"), depth)}'
    if item.get('type_node') == 'changed':
        return f'{options["gap"]}{options["negative"]}' \
               f'{item.get("key")}: ' \
               f'{stringify_v2(item.get("value1"), depth)}\n' \
               f'{options["gap"]}{options["positive"]}' \
               f'{item.get("key")}: {stringify_v2(item.get("value2"), depth)}'
