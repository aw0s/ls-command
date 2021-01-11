#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from argparse import ArgumentParser

from get_parameters_class import LFlag
from get_functions import get_size


def l_flag(args_list_arg, elements_list_arg: list, ls_path_arg: str):
    """Prints directories and files like bash -l option."""
    if not args_list_arg.all:
        elements_list = list(filter(lambda x: x[0] != '.' and x[0] != '..', elements_list_arg))
        elements_list.sort()
    else:
        elements_list = elements_list_arg

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
    parser.add_argument(type=str, dest='path', nargs='?', default=os.getcwd())

    args = parser.parse_args()

    ls_path = args.path

    if os.path.exists(ls_path):
        elements_list = ['.', '..', *os.listdir(ls_path)]

        if not args.l:
            to_print = ""
            for element in elements_list:
                if not args.all:
                    if element[0] != '.':
                        to_print = f"{to_print}  {element}"
                else:
                    to_print = f"{to_print}  {element}"

            print(to_print[2:])
        else:
            l_flag(
                args_list_arg=args,
                elements_list_arg=elements_list,
                ls_path_arg=ls_path,
            )
    else:
        print(f"{ls_path}: No such file or directory.")


if __name__ == '__main__':
    main()
