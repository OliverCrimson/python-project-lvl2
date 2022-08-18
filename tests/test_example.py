import pathlib

import gendiff.flat_differ


import os

from gendiff.convertation import convert


def testing_flat():
    if type(gendiff.flat_differ.generate_diff(
            convert(os.path.join(os.getcwd(), 'file_one.json')),
            convert(os.path.join(os.getcwd(), 'file_two.json')))) != str:
        raise Exception('asd')
    else:
        pass

def test_json(json):
    if type(json) == dict:
        print('type is ' + str(type(json)))


def test_yaml(yamol):
    if type(yamol) == dict:
        pass
