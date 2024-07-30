import argparse


def parse_args():
    '''
    Parses command-line arguments for the script.

    The function sets up the argument parser with the following options:
        - first_file: The path to the first configuration file.
        - second_file: The path to the second configuration file.
        - -f, --format: The format of the output (default: 'stylish').
            Choices are 'stylish', 'plain', and 'json'.

    Returns:
        Parsed command-line arguments.
    '''
    parser = argparse.ArgumentParser(
        description='Compares two configuration file and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f', '--format',
        default='stylish',
        choices=['stylish', 'plain', 'json'],
        help='set format of output (default: stylish)'
    )
    return parser.parse_args()
