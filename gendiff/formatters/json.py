import json


def format_json(diff):
    def walk(node):
        result = {}
        for key, content in node.items():
            status = content['status']
            if status == 'nested':
                result[key] = {
                    'status': status,
                    'children': walk(content['children'])
                }
            elif status == 'changed':
                result[key] = {
                    'status': status,
                    'old_value': content['old_value'],
                    'new_value': content['new_value']
                }
            else:
                result[key] = {
                    'status': status,
                    'value': content['value']
                }
        return result

    return json.dumps(walk(diff), indent=4)
