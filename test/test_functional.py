#!/usr/bin/env python
# coding: utf-8

import unittest
import subprocess

PROGRAM_NAME = 'main.py'

class TestCommandLine(unittest.TestCase):

    def test_help_message(self):
        # Usuario chama o programa passando o argumento '-h';
        # Programa retorna mensagem de ajuda e termina.
        call = 'python {} -h'.format(PROGRAM_NAME)
        call = call.split()
        result = subprocess.run(call, capture_output=True)
        output = result.stdout.decode('utf-8')
        self.assertIn('help', output)


if __name__ == '__main__':
    unittest.main()
