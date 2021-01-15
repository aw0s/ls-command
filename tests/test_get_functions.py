#!/usr/bin/env python
# -*- coding: utf-8 -*-

from get_functions import *


directory = 'test_examples/example_directory'
file = 'test_examples/example_file.txt'


class TestGetFunctions:
    def test_get_chmod(self):
        value_directory = get_chmod(directory)
        value_file = get_chmod(file)

        assert value_directory == 'drwxr-xr-x'
        assert value_file == '-rw-r--r--'

    def test_get_hard_links_amount(self):
        value_directory = get_hard_links_amount(directory)
        value_file = get_hard_links_amount(file)

        assert value_directory == '2'
        assert value_file == '1'

    def test_user_who_created(self):
        value_directory = user_who_created(directory)
        value_file = user_who_created(file)

        assert value_directory == 'michals'
        assert value_file == 'michals'

    def test_get_group(self):
        value_directory = get_group(directory)
        value_file = get_group(file)

        assert value_directory == 'users'
        assert value_file == 'users'

    def test_get_size(self):
        value_directory = get_size(directory)
        value_file = get_size(file)

        assert value_directory == '4096'
        assert value_file == '0'

    def test_get_date(self):
        value_directory = get_date(directory)
        value_file = get_date(file)

        assert value_directory == '01-14'
        assert value_file == '01-14'

    def test_get_time(self):
        value_directory = get_time(directory)
        value_file = get_time(file)

        assert value_directory == '22:30'
        assert value_file == '22:30'
