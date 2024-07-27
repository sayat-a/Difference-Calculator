def format_plain(diff):
    def walk(node, path):
        lines = []
        for key in sorted(node.keys()):
            status_info = node[key]
            status = status_info['status']
            current_path = f"{path}.{key}" if path else key
            if status == 'added':
                value = status_info['value']
                value_repr = format_value(value)
                lines.append(
                    f"Property '{current_path}' was added with value: "
                    f"{value_repr}")
            elif status == 'removed':
                lines.append(f"Property '{current_path}' was removed")
            elif status == 'changed':
                old_value = status_info['old_value']
                new_value = status_info['new_value']
                old_value_repr = format_value(old_value)
                new_value_repr = format_value(new_value)
                lines.append(
                    f"Property '{current_path}' was updated. From "
                    f"{old_value_repr} to {new_value_repr}")
            elif status == 'nested':
                lines.extend(walk(status_info['children'], current_path))
        return lines

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

    result = walk(diff, '')
    return '\n'.join(result)
