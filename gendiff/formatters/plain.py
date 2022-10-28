import itertools


def plain_form(tree, path=''):
    lst = []
    options = {
        'start': 'Property',
        'plus': 'was added with value:',
        'del': 'was updated. From ',
        'dddd': 'was removed'
    }
    for keys, values in tree.items():
        if values['status'] == 'got kids':
            kid = values['data']
            lst.append(plain_form(kid, path + keys + '.'))
        if values['status'] == 'deleted':
            lst.append(f"{options['start']} '{path}{keys}' {options['dddd']}")
        if values['status'] == 'different':
            lst.append(f"{options['start']} '"
                       f"{path}{keys}' {options['del']}"
                       f"{flatter(values['data1'])} "
                       f"to {flatter(values['data2'])}")
        if values['status'] == 'new':
            lst.append(f"{options['start']} '{path}{keys}' "
                       f"{options['plus']} {flatter(values['data'])}")
        qew = ''
        qew = itertools.chain(lst)
    return '\n'.join(qew)


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
