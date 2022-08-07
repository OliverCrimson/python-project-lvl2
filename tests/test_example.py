import gendiff.flat_differ
from gendiff.flat_differ import json_to_python, generate_diff, forming

# sample = gendiff.flat_differ.generate_diff(
#     json_to_python('/home/monkeybusiness/NEWNEW/python-project-lvl2/gendiff/file_one.json'),
#     json_to_python('/home/monkeybusiness/NEWNEW/python-project-lvl2/gendiff/file_two.json')
# )
def testing_flat():
    if type(gendiff.flat_differ.generate_diff(
        json_to_python('/home/monkeybusiness/NEWNEW/python-project-lvl2/gendiff/file_one.json'),
        json_to_python('/home/monkeybusiness/NEWNEW/python-project-lvl2/gendiff/file_two.json'))) != str:
        raise Exception('asd')
    else:
        pass

assert gendiff.flat_differ.generate_diff(
        json_to_python('/home/monkeybusiness/NEWNEW/python-project-lvl2/gendiff/file_one.json'),
        json_to_python('/home/monkeybusiness/NEWNEW/python-project-lvl2/gendiff/file_two.json'))[0] == '{'