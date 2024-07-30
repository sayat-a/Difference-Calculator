from gendiff.build_diff import build_diff
from gendiff.parse import load_file
from gendiff.formatters import get_formatter


def generate_diff(file1_path, file2_path, formatter='stylish'):
    '''
    Generates a difference between two configuration files.

    Parameters:
        file1_path (str): Path to the first configuration file.
        file2_path (str): Path to the second configuration file.
        formatter (str): The format of the output (default: 'stylish').
            Choices are 'stylish', 'plain', 'json'.

    Returns:
        str: The formatted difference between the two configuration files.
    '''
    data1 = load_file(file1_path)
    data2 = load_file(file2_path)
    diff = build_diff(data1, data2)
    to_format = get_formatter(formatter)
    return to_format(diff)
