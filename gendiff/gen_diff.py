from gendiff.build_diff import build_diff
from gendiff.parse import load_file
from gendiff.formatters.stylish import format_stylish
from gendiff.formatters.plain import format_plain
from gendiff.formatters.json import format_json


def generate_diff(file1_path, file2_path, formatter='stylish'):
    data1 = load_file(file1_path)
    data2 = load_file(file2_path)
    diff = build_diff(data1, data2)
    if formatter == 'stylish':
        return format_stylish(diff)
    elif formatter == 'plain':
        return format_plain(diff)
    elif formatter == 'json':
        return format_json(diff)
