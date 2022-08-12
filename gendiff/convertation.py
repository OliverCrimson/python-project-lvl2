import json
import yaml


def convert(file):
    if file.endswith('.json'):
        with open(file, "r") as some_file:
            result = json.load(some_file)
        return result
    if file.endswith('.yaml') or file.endswith('.yml'):
        with open(file) as some_file:
            result = yaml.safe_load(some_file)
            return result
    else:
        raise Exception(f'file {file} has unsupported format.')