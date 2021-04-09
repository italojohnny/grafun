#!/usr/bin/env python
# coding: utf-8

import subprocess
import os
from test import *


class TestCommandLine(unittest.TestCase):


    def setUp(self):
        self.remove_file(OUTPUT_IMAGE)


    def remove_file(self, file_name):
        if pathlib.Path(file_name).is_file():
            os.remove(file_name)

    def execute(self, command: str):
        result = subprocess.run(command.split(), capture_output=True)
        outcod = result.returncode
        output = result.stdout.decode('utf-8')
        outerr = result.stderr.decode('utf-8')
        return (output, outerr, outcod)


    def assertIsFile(self, name: str):
        path = pathlib.Path(name)
        self.assertTrue(
            path.is_file(), 'Arquivo "{}" nao existe'.format(str(path))
        )


    def test_help_message(self):
        # Usuario chama o programa passando o argumento '-h';
        # Programa retorna mensagem de ajuda e termina.
        call = 'python {} -h'.format(PROGRAM_NAME)
        output, _, _ = self.execute(call)
        self.assertIn('help', output)


    def test_output_image(self):
        # Usuario chama o programa passando um arquivo com funcoes:
        # Programa gera um arquivo de imagem png
        call = 'python {} {}'.format(PROGRAM_NAME, PROGRAM_NAME)
        self.execute(call)
        self.assertIsFile(OUTPUT_IMAGE)


if __name__ == '__main__':
    unittest.main()
