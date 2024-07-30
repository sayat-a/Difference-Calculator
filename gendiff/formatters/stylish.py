import json


def format_stylish(diff, depth=1):
    '''
    Formats a diff's dictionary into a stylish format for a readable output.

    Parameters:
        diff (dict): The diff dictionary representing the differences between
            two data dictionaries.
        depth (int): The current depth for indentation. Defaults to 1.

    Returns:
        str: A formatted string representing the differences in a stylish
            format.
    '''
    indent_size = 4
    deep_indent_size = indent_size * depth
    current_indent = ' ' * (deep_indent_size - 2)
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
    '''
    Additional function for 'format_stylish' function
    Formats a value for the stylish diff output.

    Parameters:
        value (any): The value to format. Can be a nested dictionary.
        depth (int): The current depth for indentation.

    Returns:
        str: A formatted string representation of the value.
    '''
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
