#!/usr/bin/env python
# -*- coding: utf-8 -*-

from get_functions import *


class LFlag:
    def __init__(self, path: str, chars_max: int, element: str):
        self.path = path
        self.chars_max = chars_max

        self.chmod = ""
        self.hard_links = ""
        self.user = ""
        self.group = ""
        self.kilobytes = ""
        self.date = ""
        self.hour = ""
        self.element = element

        self.to_print = ""

    def generate_parameters(self, path: str, chars_max: int) -> str:
        self.chmod = get_chmod(path)
        self.hard_links = get_hard_links_amount(path)
        self.user = user_who_created(path)
        self.group = get_group(path)
        self.kilobytes = get_size(path)
        self.date = get_date(path)
        self.hour = get_time(path)

        if len(str(self.kilobytes)) < chars_max:
            difference = chars_max - len(str(self.kilobytes))
        else:
            difference = 0

        spaces = difference * ' '

        to_print = f"{self.chmod} {self.hard_links} {self.user} {self.group} {spaces}{self.kilobytes} {self.date} {self.hour} {self.element}"

        return to_print

    def __str__(self) -> str:
        return self.generate_parameters(self.path, self.chars_max)
