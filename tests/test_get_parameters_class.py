#!/usr/bin/env python
# -*- coding: utf-8 -*-

from get_parameters_class import LFlag


def test_get_parameter_class():
    correct_line_directory = 'drwxr-xr-x 2 michals users 4096 01-14 22:30 example_directory'
    correct_line_file = '-rw-r--r-- 1 michals users    0 01-14 22:30 example_file.txt'

    generated_line_directory = str(LFlag('test_examples/example_directory', 4, 'example_directory'))
    generated_line_file = str(LFlag('test_examples/example_file.txt', 4, 'example_file.txt'))

    assert generated_line_directory == correct_line_directory
    assert generated_line_file == correct_line_file
