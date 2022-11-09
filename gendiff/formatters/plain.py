def flatter(data):
    if isinstance(data, dict):
        return '[complex value]'
    if isinstance(data, bool):
        return str(data).lower()
    if data is None:
        return 'null'
    if isinstance(data, str):
        return f"'{data}'"
    else:
        return data


def plain_form(tree, path=''):
    options = {
        'start': 'Property',
        'plus': 'was added with value:',
        'del': 'was updated. From ',
        'rem': 'was removed'
    }
    children = tree.get('children')

    if tree['type_node'] == 'root':
        string = map(lambda x: plain_form(x, f'{path}'), children)
        return '\n'.join(filter(bool, string))
    if tree['type_node'] == 'nested':
        string = map(lambda x: plain_form(x, f'{path}{tree["key"]}.'), children)
        return '\n'.join(filter(bool, string))
    if tree['type_node'] == 'new':
        string = flatter(tree["value"])
        string = f"{options['start']} '{path}{tree['key']}'" \
                 f" {options['plus']} {string}"
        return string
    if tree['type_node'] == 'deleted':
        return f"{options['start']} '{path}{tree['key']}' {options['rem']}"
    if tree['type_node'] == 'changed':
        return f"{options['start']} '{path}{tree['key']}' "\
               f"{options['del']}{flatter(tree['value1'])}"\
               f' to {flatter(tree["value2"])}'
