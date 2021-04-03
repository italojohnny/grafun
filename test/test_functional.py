#!/usr/bin/env python
# coding: utf-8

import unittest
import subprocess
import pathlib

PROGRAM_NAME = 'main.py'
EXAMPLE_FILE = 'resource/script.py'
OUTPUT_IMAGE = 'output.png'

class TestCommandLine(unittest.TestCase):

    def test_help_message(self):
        # Usuario chama o programa passando o argumento '-h';
        # Programa retorna mensagem de ajuda e termina.
        call = 'python {} -h'.format(PROGRAM_NAME)
        call = call.split()
        result = subprocess.run(call, capture_output=True)
        output = result.stdout.decode('utf-8')
        self.assertIn('help', output)


    def test_output_image(self):
        # Usuario chama o programa passando um arquivo com funcoes:
        # Programa gera um arquivo de imagem png
        path = pathlib.Path(EXAMPLE_FILE)
        self.assertTrue(path.is_file())

        call = 'python {} {}'.format(PROGRAM_NAME, EXAMPLE_FILE)
        call = call.split()
        result = subprocess.run(call, capture_output=True)

        path = pathlib.Path(OUTPUT_IMAGE)
        self.assertTrue(path.is_file())


if __name__ == '__main__':
    unittest.main()
