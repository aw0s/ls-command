#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from argparse import ArgumentParser


def l_flag(args_list_arg, dirs_list_arg: list, files_list_arg: list, ls_path_arg: str) -> str:
    """Returns string to print (-l flag)."""
    if args_list_arg.all:
        pass
    else:
        dirs_list_arg = list(filter((lambda x: x[0] != '.'), dirs_list_arg))
        files_list_arg = list(filter((lambda x: x[0] != '.'), files_list_arg))

    return f"{dirs_list_arg, files_list_arg}"


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

        print(dirs_list)

        if not args.l:
            to_print = ""
            for directory in dirs_list:
                if not args.all:
                    if directory[0] != '.':
                        to_print = f"{to_print}\t{directory}"
                else:
                    to_print = f"{to_print}\t{directory}"

            for file in files_list:
                if not args.all:
                    if file[0] != '.':
                        to_print = f"{to_print}\t{file}"
                else:
                    to_print = f"{to_print}\t{file}"

            print(to_print[1:])
            # "1:" because the first character is a tabulator
        else:
            print(l_flag(
                args_list_arg=args,
                dirs_list_arg=dirs_list,
                files_list_arg=files_list,
                ls_path_arg=ls_path,
            ))
    else:
        print(f"{ls_path}: No such file or directory.")


if __name__ == '__main__':
    main()
