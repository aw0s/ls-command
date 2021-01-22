#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""get_functions imports also os, from stat filemode, from pwd getpwuid and from grp getgrgid"""
from get_functions import *


class LOFlag:
    def __init__(self, path: str, element: str, args, max_chars_dict: dict):
        self.path = path
        self.element = element
        self.args = args
        self.max_chars_dict = max_chars_dict

        self.chmod = ""
        self.hard_links = ""
        self.user = ""
        self.group = ""
        self.size = ""
        self.date = ""
        self.hour = ""

        self.to_print = ""

    def generate_parameters(self, path: str, max_chars_dict: dict) -> str:
        self.chmod = get_chmod(path)
        self.hard_links = get_hard_links_amount(path)
        self.user = user_who_created(path)
        self.group = get_group(path)
        self.size = get_size(path)
        self.date = get_date(path)
        self.hour = get_time(path)

        if len(str(self.hard_links)) < max_chars_dict['hard_links']:
            difference = max_chars_dict['hard_links'] - len(str(self.hard_links))
        else:
            difference = 0
        hard_links_spaces = difference * ' '

        if len(str(self.user)) < max_chars_dict['user']:
            difference = max_chars_dict['user'] - len(str(self.user))
        else:
            difference = 0
        user_spaces = difference * ' '

        if len(str(self.group)) < max_chars_dict['group']:
            difference = max_chars_dict['group'] - len(str(self.group))
        else:
            difference = 0
        group_spaces = difference * ' '

        if len(str(self.size)) < max_chars_dict['size']:
            difference = max_chars_dict['size'] - len(str(self.size))
        else:
            difference = 0
        size_spaces = difference * ' '

        if self.args.o:
            to_print = f"{self.chmod} {hard_links_spaces}{self.hard_links} {user_spaces}{self.user} {size_spaces}{self.size} {self.date} {self.hour} {self.element}"
        else:
            to_print = f"{self.chmod} {hard_links_spaces}{self.hard_links} {user_spaces}{self.user} {group_spaces}{self.group} {size_spaces}{self.size} {self.date} {self.hour} {self.element}"
        if os.path.islink(path):
            to_print += f" -> {os.path.realpath(path)}"

        return to_print

    def __str__(self) -> str:
        return self.generate_parameters(self.path, self.max_chars_dict)
