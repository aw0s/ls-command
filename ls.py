#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from argparse import ArgumentParser
from string import printable, digits, ascii_letters

from get_parameters_class import LFlag
from get_functions import get_size


def l_flag(args_arg, elements_list_arg: list, ls_path_arg: str):
    """Prints directories and files like bash -l option."""
    if not args_arg.all:
        elements_list = list(filter(lambda x: x[0] != '.' and x[:2] != '..', elements_list_arg))
    else:
        elements_list = elements_list_arg

    if not args_arg.t:
        """Sorting the list only by letters and digits."""
        words = printable
        words = words.replace(digits + ascii_letters, "")

        alphabet_dict = {element: element.lstrip(words) for element in elements_list}
        alphabet_dict = dict(sorted(list(alphabet_dict.items()), key=lambda x: x[1].lower()))
        elements_list = list(alphabet_dict.keys())

    chars_max = 0
    for element in elements_list:
        element_path = os.path.join(ls_path_arg, element)
        if (element_size := len(str(get_size(element_path)))) > chars_max:
            chars_max = element_size

        file_or_dir = LFlag(element_path, chars_max, element)
        print(str(file_or_dir))


def main():
    parser = ArgumentParser()

    parser.add_argument('-a', '--all', action='store_true')
    parser.add_argument('-l', action='store_true')
    parser.add_argument('-t', action='store_true')
    parser.add_argument(type=str, dest='path', nargs='?', default=os.getcwd())

    args = parser.parse_args()

    ls_path = args.path
    if os.path.exists(ls_path):
        elements_list = sorted(['.', '..', *os.listdir(ls_path)], key=str.lower)

        time_dict = {x: round(os.path.getmtime(os.path.join(ls_path, x))) for x in elements_list}
        time_sorted_dict = {
            key: value for key, value in sorted(
                time_dict.items(), key=(lambda item: item[1]), reverse=True
            )
        }
        words = printable
        words = words.replace(digits + ascii_letters, "")

        alphabet_dict = {element: element.lstrip(words) for element in elements_list}
        alphabet_dict = dict(sorted(list(alphabet_dict.items()), key=lambda x: x[1].lower()))
        elements_list = list(alphabet_dict.keys())

        if not args.all:
            if args.t:
                time_sorted_list = list(filter((lambda x: x[0] != '.' and x[:2] != '..'), time_sorted_dict.keys()))
                chosen_list = time_sorted_list.copy()
            else:
                elements_list_not_all = list(filter((lambda x: x[0] != '.' and x[:2] != '..'), elements_list))
                chosen_list = elements_list_not_all.copy()
        else:
            if args.t:
                time_sorted_list = list(filter((lambda x: x[0] != '.' and x[:2] != '..'), time_sorted_dict.keys()))
                chosen_list = time_sorted_list.copy()
            else:
                elements_list_not_all = list(filter((lambda x: x[0] != '.' and x[:2] != '..'), elements_list))
                chosen_list = elements_list_not_all.copy()

        if not args.l:
            to_print = ""
            for element in chosen_list:
                to_print = f"{to_print}  {element}"

            print(to_print[2:])
        else:
            l_flag(
                args_arg=args,
                elements_list_arg=chosen_list,
                ls_path_arg=ls_path,
            )
    else:
        print(f"{ls_path}: No such file or directory.")


if __name__ == '__main__':
    main()
