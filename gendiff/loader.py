import json
import yaml


def get_data(file_path):
    with open(file_path) as data:
        return parse(data, get_file_format(file_path))


def parse(data, format_name):
    if format_name == 'json':
        return json.load(data)
    if format_name == 'yaml':
        return yaml.safe_load(data)
    else:
        raise Exception(f"{format_name} has unsupported format")


def get_file_format(file):
    if file.endswith('.json'):
        return 'json'
    if file.endswith('.yaml') or file.endswith('.yml'):
        return 'yaml'
    else:
        raise Exception("File has unsupported format")
