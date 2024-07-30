import json
import yaml
import os


def define_extension(file_path):
    path, extension = os.path.splitext(file_path)
    return extension


def load_file(file_path):
    extension = define_extension(file_path)
    with open(file_path) as file:
        if extension == '.json':
            return json.load(file)
        elif extension == '.yaml' or extension == '.yml':
            return yaml.safe_load(file)
        else:
            raise ValueError(f'Unsupported extension {extension}')
