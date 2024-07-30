import json
import yaml
import os


def define_extension(file_path):
    '''
    Defines file's extension

    Parameter:
        file_path (str): Path to the file

    Returns:
        str: extension of the file
    '''
    path, extension = os.path.splitext(file_path)
    return extension


def load_file(file_path):
    '''
    Loads and parses a configuration file.

    Parameters:
        file_path (str): Path to the configuration file.

    Returns:
        dict: Parsed content of the file.

    Raises:
        ValueError: If the file extension is not supported.
    '''
    extension = define_extension(file_path)
    with open(file_path) as file:
        if extension == '.json':
            return json.load(file)
        elif extension == '.yaml' or extension == '.yml':
            return yaml.safe_load(file)
        else:
            raise ValueError(f'Unsupported extension {extension}')
