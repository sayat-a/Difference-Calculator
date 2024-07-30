import json


def format_json(diff):
    '''
    Formats a diff's dictionary into a JSON string.

    Parameters:
        diff (dict): The diff dictionary representing the differences between
            two data dictionaries.

    Returns:
        str: A JSON formatted string representing the diff.
    '''
    return json.dumps(diff, indent=4)
