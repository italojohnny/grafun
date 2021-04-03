#!/usr/bin/env python
# coding: utf-8

import unittest
import main
import sys

OUTPUT_FILE = 'output.txt'

class TestMain(unittest.TestCase):

    def setUp(self):
        sys.stdout = open(OUTPUT_FILE, 'w')

    def tearDown(self):
        sys.stdout.close()

    def test_help_message(self):
        parser = main.get_argparse()

        try:
            parser.parse_args(['-h'])
        except:
            pass # silencia saida abrupta

        sys.stdout.close()
        with open(OUTPUT_FILE, 'r') as output_file:
            help_message = output_file.read()
            self.assertIn('help message', help_message)
