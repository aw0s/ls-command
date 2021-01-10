#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import path
from argparse import ArgumentParser
from string import ascii_lowercase, ascii_uppercase

from get_functions import *


def l_flag(args_list_arg, dirs_list_arg: list, files_list_arg: list, ls_path_arg: str):
    """Prints directories and files like bash -l option."""
    if not args_list_arg.all:
        dirs_list = list(filter(lambda x: x[0] != '.', dirs_list_arg))
        files_list = list(filter(lambda x: x[0] != '.', files_list_arg))

        dirs_list.sort()
        files_list.sort()
    else:
        dirs_list = dirs_list_arg
        files_list = files_list_arg

    for directory in dirs_list:
        directory_path = path.join(ls_path_arg, directory)

        chmod = get_chmod(directory_path)
        hard_links = get_hard_links_amount(directory_path)
        user = user_who_created(directory_path)
        group = get_group(directory_path)
        kilobytes = get_size(directory_path)
        date = get_date(directory_path)
        hour = get_time(directory_path)

        print(f"{chmod} {hard_links} {user} {group} {kilobytes} {date} {hour} {directory}")

    for file in files_list:
        file_path = os.path.join(ls_path_arg, file)

        chmod = get_chmod(file)
        hard_links = get_hard_links_amount(file_path)
        user = user_who_created(file_path)
        group = get_group(file_path)
        kilobytes = get_size(file_path)
        date = get_date(file_path)
        hour = get_time(file_path)

        print(f"{chmod} {hard_links} {user} {group} {kilobytes} {date} {hour} {file}")


def main():
    parser = ArgumentParser()

    parser.add_argument('-a', '--all', action='store_true')
    parser.add_argument('-l', action='store_true')
    parser.add_argument(type=str, dest='path', nargs='?', default=os.getcwd())

    args = parser.parse_args()

    ls_path = args.path

    if os.path.exists(ls_path):
        dirs_list, files_list = [], []
        for _ in os.listdir(ls_path):
            if os.path.isdir(os.path.join(ls_path, _)):
                dirs_list.append(_)
            elif os.path.isfile(os.path.join(ls_path, _)):
                files_list.append(_)

        if not args.l:
            to_print = ""
            for directory in dirs_list:
                if not args.all:
                    if directory[0] != '.':
                        to_print = f"{to_print}  {directory}"
                else:
                    to_print = f"{to_print}  {directory}"

            for file in files_list:
                if not args.all:
                    if file[0] != '.':
                        to_print = f"{to_print}  {file}"
                else:
                    to_print = f"{to_print}  {file}"

            print(to_print[2:])
        else:
            l_flag(
                args_list_arg=args,
                dirs_list_arg=dirs_list,
                files_list_arg=files_list,
                ls_path_arg=ls_path,
            )
    else:
        print(f"{ls_path}: No such file or directory.")


if __name__ == '__main__':
    main()
