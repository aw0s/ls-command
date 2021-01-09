#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from argparse import ArgumentParser


def l_flag(args_list_arg, dirs_list_arg: list, files_list_arg: list, ls_path_arg: str):
    """Prints directories and files like bash -l option."""
    if not args_list_arg.all:
        dirs_list = list(filter(lambda x: x[0] != '.', dirs_list_arg))
        files_list = list(filter(lambda x: x[0] != '.', files_list_arg))
    else:
        dirs_list = dirs_list_arg
        files_list = files_list_arg

    for directory in dirs_list:
        chmod = os.popen(f'''ls -l {ls_path_arg} | grep {directory} |  cut -d ' ' -f 1''').read().strip()
        hard_links = os.popen(f'''ls -l {ls_path_arg} | grep {directory} |  cut -d ' ' -f 2''').read().strip()
        user = os.popen(f'''ls -l {ls_path_arg} | grep {directory} |  cut -d ' ' -f 3''').read().strip()
        group = os.popen(f'''ls -l {ls_path_arg} | grep {directory} |  cut -d ' ' -f 4''').read().strip()
        kilobytes = os.popen(f'''ls -l {ls_path_arg} | grep {directory} |  cut -d ' ' -f 5''').read().strip()
        date = os.popen(f'''ls -l {ls_path_arg} | grep {directory} |  cut -d ' ' -f 6''').read().strip()
        hour = os.popen(f'''ls -l {ls_path_arg} | grep {directory} |  cut -d ' ' -f 7''').read().strip()
        dir_name = os.popen(f'''ls -l {ls_path_arg} | grep {directory} |  cut -d ' ' -f 8''').read().strip()

        print(f"{chmod} {hard_links} {user} {group} {kilobytes} {date} {hour} {dir_name}")

    for file in files_list:
        chmod = os.popen(f'''ls -l {ls_path_arg} | grep {file} |  cut -d ' ' -f 1''').read().strip()
        hard_links = os.popen(f'''ls -l {ls_path_arg} | grep {file} |  cut -d ' ' -f 2''').read().strip()
        user = os.popen(f'''ls -l {ls_path_arg} | grep {file} |  cut -d ' ' -f 3''').read().strip()
        group = os.popen(f'''ls -l {ls_path_arg} | grep {file} |  cut -d ' ' -f 4''').read().strip()
        kilobytes = os.popen(f'''ls -l {ls_path_arg} | grep {file} |  cut -d ' ' -f 5''').read().strip()
        date = os.popen(f'''ls -l {ls_path_arg} | grep {file} |  cut -d ' ' -f 6''').read().strip()
        hour = os.popen(f'''ls -l {ls_path_arg} | grep {file} |  cut -d ' ' -f 7''').read().strip()
        file_name = os.popen(f'''ls -l {ls_path_arg} | grep {file} |  cut -d ' ' -f 8''').read().strip()

        print(f"{chmod} {hard_links} {user} {group} {kilobytes} {date} {hour} {file_name}")


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
