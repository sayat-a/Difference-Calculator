def format_plain(diff):
    result = walk(diff, '')
    return '\n'.join(result)


def walk(node, path):
    lines = []
    for key in sorted(node.keys()):
        status_info = node[key]
        status = status_info['status']
        current_path = f"{path}.{key}" if path else key
        lines.extend(process_status(status, status_info, current_path))
    return lines


def process_status(status, status_info, current_path):
    if status == 'added':
        return [format_added(current_path, status_info['value'])]
    elif status == 'removed':
        return [format_removed(current_path)]
    elif status == 'changed':
        return [format_changed(current_path, status_info)]
    elif status == 'nested':
        return walk(status_info['children'], current_path)
    return []


def format_added(current_path, value):
    return f"Property '{current_path}' was added with value: " \
           f"{format_value(value)}"


def format_removed(current_path):
    return f"Property '{current_path}' was removed"


def format_changed(current_path, status_info):
    old_value = format_value(status_info['old_value'])
    new_value = format_value(status_info['new_value'])
    return f"Property '{current_path}' was updated. From {old_value} to " \
           f"{new_value}"


def format_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, str):
        return f"'{value}'"
    elif value is None:
        return 'null'
    elif isinstance(value, bool):
        return str(value).lower()
    else:
        return str(value)
