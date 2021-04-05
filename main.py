#!/usr/bin/env python
# coding: utf-8

import argparse
import pathlib
import os
import mimetypes

def get_argparse():
    parser = argparse.ArgumentParser(
        prog = 'grafun',
        description = 'creates function call graph.',
        epilog = 'for more access: https://github.com/italojohnny/grafun'
    )
    parser.add_argument(
        nargs='*',
        dest='paths',
        default=[pathlib.Path().absolute()],
        type=pathlib.Path,
        help='list of directories and files',
    )
    return parser


def filter_python_extension(file):
    if pathlib.Path(file).suffix == '.py':
        return True
    return False


def get_file_list(paths):
    all_files = list()

    for path in paths:
        for root, _, files in os.walk(path):
            for file in files:
                full_file_name = os.path.join(root, file)
                guess_type = mimetypes.guess_type(full_file_name)[0]

                if guess_type and guess_type.startswith('text'):
                    all_files.append(full_file_name)

    return all_files

def main():
    args = get_argparse().parse_args()
    files = get_file_list(args.paths)

if __name__ == '__main__':
    main()
