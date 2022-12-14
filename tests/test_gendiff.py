import pytest
import pathlib

from gendiff import generate_diff


@pytest.mark.parametrize(
    'file1, file2, expected_result, form',
    [('file1tree.json', 'file2tree.json', 'tree_result_example.txt', 'stylish'),
     ('file1tree.json', 'file2tree.json', 'plain_form_example.txt', 'plain'),
     ('file1tree.yaml', 'file2tree.yaml', 'tree_result_example.txt', 'stylish'),
     ('file1tree.yaml', 'file2tree.yaml', 'plain_form_example.txt', 'plain'),
     ('file1tree.json', 'file2tree.json', 'json_form_example.txt', 'json')]
)
def test_tree(file1, file2, expected_result, form):
    home_dir = str(pathlib.Path.cwd())
    f1 = f'{home_dir}/tests/fixtures/{file1}'
    f2 = f'{home_dir}/tests/fixtures/{file2}'
    with open(f'{home_dir}/tests/fixtures/{expected_result}') as data:
        expected = data.read()
        assert generate_diff(f1, f2, form) == expected
