import pathlib

import gendiff.flat_differ
from gendiff.flat_differ import json_to_python, generate_diff, forming

import os

def testing_flat():
    if type(gendiff.flat_differ.generate_diff(
            json_to_python(os.path.join(os.getcwd(), 'file_one.json')),
            json_to_python(os.path.join(os.getcwd(), 'file_two.json')))) != str:
        raise Exception('asd')
    else:
        pass

