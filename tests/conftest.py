import pytest
import os
from gendiff.convertation import convert


@pytest.fixture
def json():
    data = convert('file_one.json')
    return data


@pytest.fixture()
def yamol():
    data2 = convert('gendiff/file_one.yaml')
    return data2
