#!/usr/bin/env python
# coding: utf-8

import argparse

def get_argparse():
    return argparse.ArgumentParser()

if __name__ == '__main__':
    a = get_argparse().parse_args(['-h'])
