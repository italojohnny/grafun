#!/usr/bin/env python
# coding: utf-8

import unittest
import main
import sys
import pathlib

PROGRAM_NAME = 'main.py'
OUTPUT_FILE = 'output.txt'

class TestMain(unittest.TestCase):

    def setUp(self):
        sys.stdout = open(OUTPUT_FILE, 'w')

    def tearDown(self):
        sys.stdout.close()

    def test_help_message(self):
        """
        testa se parse gera mensagem de ajuda
        """
        parser = main.get_argparse()

        try:
            parser.parse_args(['-h'])
        except:
            pass # silencia saida abrupta

        sys.stdout.close()
        with open(OUTPUT_FILE, 'r') as output_file:
            help_message = output_file.read()
            self.assertIn('help message', help_message)

    def test_input_paths(self):
        """
        testa se argumento de entrada e igual ao argumento parseado
        """
        input_paths = ['test/resource/script.py']
        parser = main.get_argparse()
        args = parser.parse_args(input_paths)
        paths = [str(x) for x in args.paths]
        self.assertEqual(set(paths), set(input_paths))


    def test_get_file_list(self):
        """
        testa se retornar lista de arquivos
        """
        input_files = [PROGRAM_NAME]
        input_dirs = ['test/']
        input_paths = input_files + input_dirs

        parser = main.get_argparse()
        args = parser.parse_args(input_paths)
        all_files = main.get_file_list(args.paths)

        # verifica se todos os valores sao arquivos
        self.assertTrue(all([pathlib.Path(x).is_file() for x in all_files]))

        # verifica se os arquivos passados na linha de comando sao preservados
        self.assertTrue(all([pathlib.Path(i) in all_files for i in input_files]))


    def test_filter_python_extension(self):
        """
        testa se filtra apenas arquivos python
        """
        all_files = [
            'file.txt',
            'file.py',
            'file.html',
            'file.cpp',
            'file.c',
        ]
        filtered_files = set(['file.py'])
        result = set(filter(main.filter_python_extension, all_files))
        self.assertEqual(result, filtered_files)
