#!/usr/bin/env python3
import argparse
from gendiff.gen_diff import generate_diff


def main():
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
    args = parser.parse_args()
    print(generate_diff(
        args.first_file, args.second_file, formatter=args.format))


if __name__ == '__main__':  
    main()
