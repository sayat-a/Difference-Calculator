from gendiff.build_diff import build_diff
from gendiff.parse import load_file
from gendiff.formatters.stylish import format_stylish


def generate_diff(file1_path, file2_path, formatter='stylish'):
    data1 = load_file(file1_path)
    data2 = load_file(file2_path)
    if data1 is None:
        data1 = {}
    if data2 is None:
        data2 = {}
    diff = build_diff(data1, data2)
    if formatter == 'stylish':
        return format_stylish(diff)
