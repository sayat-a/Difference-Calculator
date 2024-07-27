import json
from . import parse


def build_diff(data1, data2):
    diff = {}
    all_keys = sorted(set(data1.keys()).union(set(data2.keys())))
    for key in all_keys:
        if key not in data2:
            diff[key] = {'status': 'removed', 'value': data1[key]}
        elif key not in data1:
            diff[key] = {'status': 'added', 'value': data2[key]}
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            diff[key] = {
                'status': 'nested',
                'children': build_diff(data1[key], data2[key])
            }
        elif data1[key] != data2[key]:
            diff[key] = {
                'status': 'changed',
                'old_value': data1[key],
                'new_value': data2[key]
            }
        else:
            diff[key] = {'status': 'unchanged', 'value': data1[key]}
    return diff


def format_stylish(diff, depth=1):
    indent_size = 4
    deep_indent_size = indent_size * depth
    current_indent = ' ' * deep_indent_size
    bracket_indent = ' ' * (deep_indent_size - indent_size)
    lines = []
    for key, value in diff.items():
        status = value['status']
        if status == 'added':
            lines.append(
                f"{current_indent}+ {key}: "
                f"{format_value(value['value'], depth + 1)}"
            )
        elif status == 'removed':
            lines.append(
                f"{current_indent}- {key}: "
                f"{format_value(value['value'], depth + 1)}"
            )
        elif status == 'changed':
            lines.append(
                f"{current_indent}- {key}: "
                f"{format_value(value['old_value'], depth + 1)}"
            )
            lines.append(
                f"{current_indent}+ {key}: "
                f"{format_value(value['new_value'], depth + 1)}"
            )
        elif status == 'nested':
            nested_lines = format_stylish(value['children'], depth + 1)
            lines.append(f"{current_indent}  {key}: {nested_lines}")
        else:  # 'unchanged'
            lines.append(
                f"{current_indent}  {key}: "
                f"{format_value(value['value'], depth + 1)}"
            )
    result = "\n".join(lines)
    return f"{{\n{result}\n{bracket_indent}}}"


def format_value(value, depth):
    if isinstance(value, dict):
        indent_size = 4
        deep_indent_size = indent_size * depth
        current_indent = ' ' * deep_indent_size
        bracket_indent = ' ' * (deep_indent_size - indent_size)
        lines = []
        for key, val in value.items():
            lines.append(
                f"{current_indent}{key}: {format_value(val, depth + 1)}"
            )
        result = "\n".join(lines)
        return f"{{\n{result}\n{bracket_indent}}}"
    else:
        return json.dumps(value, ensure_ascii=False).replace('"', '')


def format_diff(diff, depth=1):
    indent = '    ' * depth
    diff_lines = []
    for key, info in sorted(diff.items()):
        status = info['status']
        if status == 'removed':
            diff_lines.append(
                f"{indent}  - {key}: {json.dumps(info['value'])}"
            )
        elif status == 'added':
            diff_lines.append(
                f"{indent}  + {key}: {json.dumps(info['value'])}"
            )
        elif status == 'changed':
            diff_lines.append(
                f"{indent}  - {key}: {json.dumps(info['old_value'])}"
            )
            diff_lines.append(
                f"{indent}  + {key}: {json.dumps(info['new_value'])}"
            )
        elif status == 'nested':
            nested_diff = format_diff(info['children'], depth + 1)
            diff_lines.append(f"{indent}    {key}: {nested_diff}")
        else:  # 'unchanged'
            diff_lines.append(
                f"{indent}    {key}: {json.dumps(info['value'])}"
            )
    return "{\n" + "\n".join(
        diff_lines).replace('"', '') + f"\n{'    ' * (depth - 1)}}}"


def generate_diff(file1_path, file2_path, formatter='stylish'):
    data1 = parse.load_file(file1_path)
    data2 = parse.load_file(file2_path)
    if data1 is None:
        data1 = {}
    if data2 is None:
        data2 = {}
    diff = build_diff(data1, data2)
    if formatter == 'stylish':
        return format_stylish(diff)
