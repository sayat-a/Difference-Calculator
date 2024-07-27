import json
import yaml


def define_extension(file_path):
    return str(file_path)[-4:]


def load_file(file_path):
    extension = define_extension(file_path)
    with open(file_path) as file:
        if extension == 'json':
            return json.load(file)
        elif extension == 'yaml' or extension == 'yml':
            return yaml.safe_load(file)
