#!/usr/bin/env python3
from gendiff.gen_diff import generate_diff
from gendiff.cli import parse_args


def main():
    '''
    Main function to parse command-line arguments and generate the difference
    between two files.

    This function uses argparse to handle command-line arguments for specifying
    the two files to compare and the desired output format. It then generates
    and prints the difference using the specified format.

    Parameters (command-line arguments):
        first_file (str): The path to the first file to compare.
        second_file (str): The path to the second file to compare.
        -f, --format (str): The format for the output (default: 'stylish').
            Choices: ['stylish', 'plain', 'json'].
    '''
    args = parse_args()
    print(generate_diff(
        args.first_file, args.second_file, formatter=args.format))


if __name__ == '__main__':
    main()
