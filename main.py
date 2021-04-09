#!/usr/bin/env python
# coding: utf-8

import argparse
import pathlib
import os
import mimetypes
import graphviz

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
        if pathlib.Path(path).is_file():
            all_files.append(path)

        else:
            for root, _, files in os.walk(path):
                for file in files:
                    all_files.append(os.path.join(root, file))

    return list(filter(filter_python_extension, all_files))


def main():
    args = get_argparse().parse_args()
    files = get_file_list(args.paths)

    digraph = graphviz.Digraph()
    digraph.render(filename='output', cleanup=True, format='png')

if __name__ == '__main__':
    main()
