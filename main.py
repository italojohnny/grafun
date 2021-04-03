#!/usr/bin/env python
# coding: utf-8

import argparse
import pathlib

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

if __name__ == '__main__':
    a = get_argparse().parse_args(['-h'])
