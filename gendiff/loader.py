import json
import yaml


def load_file(file):
    if file.endswith('.json'):
        return json_extractor(file)
    elif file.endswith('.yaml') or file.endswith('.yml'):
        return yaml_extractor(file)
    else:
        raise Exception(f"{file} has unsupported format.")


def json_extractor(file):
    with open(file, "r") as data:
        return json.load(data)


def yaml_extractor(file):
    with open(file, "r") as data:
        return yaml.safe_load(data)
