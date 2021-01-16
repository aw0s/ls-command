#!/usr/bin/env python
# -*- coding: utf-8 -*-

from get_functions import *


class LFlag:
    def __init__(self, path: str, chars_max: int, element: str):
        self.path = path
        print(self.path)
        self.chars_max = chars_max
        self.element = element

        self.chmod = ""
        self.hard_links = ""
        self.user = ""
        self.group = ""
        self.kilobytes = ""
        self.date = ""
        self.hour = ""

        self.to_print = ""

    def generate_parameters(self, path: str, chars_max: int) -> str:
        self.chmod = get_chmod(path)
        self.hard_links = get_hard_links_amount(path)
        self.user = user_who_created(path)
        self.group = get_group(path)
        self.kilobytes = get_size(path)
        self.date = get_date(path)
        self.hour = get_time(path)

        chmod_chars_max = len(get_chmod())
        if len(self.chmod) < chars_max:
            chmod_difference = chars_max - len(self.chmod)
        else:
            chmod_difference = 0
        chmod_spaces = chmod_difference * ' '

        if len(self.hard_links) < chars_max:
            hard_links_difference = chars_max - len(self.hard_links)
        else:
            hard_links_difference = 0
        hard_links_spaces = hard_links_difference * ' '

        if len(self.user) < chars_max:
            user_difference = chars_max - len(self.user)
        else:
            user_difference = 0
        user_spaces = user_difference * ' '

        if len(self.group) < chars_max:
            group_difference = chars_max - len(self.group)
        else:
            group_difference = 0
        group_spaces = group_difference * ' '

        if len(self.kilobytes) < chars_max:
            kilobytes_difference = chars_max - len(self.kilobytes)
        else:
            kilobytes_difference = 0
        kilobytes_spaces = kilobytes_difference * ' '

        if len(self.date) < chars_max:
            date_difference = chars_max - len(self.date)
        else:
            date_difference = 0
        date_spaces = date_difference * ' '

        if len(self.hour) < chars_max:
            hour_difference = chars_max - len(self.hour)
        else:
            hour_difference = 0
        hour_spaces = hour_difference * ' '

        to_print = f"{chmod_spaces}{self.chmod} {hard_links_spaces}{self.hard_links} {user_spaces}{self.user} {group_spaces}{self.group} {kilobytes_spaces}{self.kilobytes} {date_spaces}{self.date} {hour_spaces}{self.hour} {self.element}"

        return to_print

    def __str__(self) -> str:
        return self.generate_parameters(self.path, self.chars_max)
