import json
import yaml


def define_extension(file_path):
    return file_path[-4:]


def load_file(file_path):
    extension = define_extension(file_path)
    with open(file_path, 'r', encoding='utf-8') as file:
        if extension == 'json':
            return json.load(file)
        elif extension in ['.yml', 'yaml']:
            return yaml.safe_load(file)
