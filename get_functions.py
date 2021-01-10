#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from stat import filemode
from pwd import getpwuid
from grp import getgrgid

from datetime import datetime


def get_chmod(path: str) -> str:
    file_status = os.stat(path)
    chmod = filemode(file_status.st_mode)

    return chmod


def get_hard_links_amount(path: str) -> str:
    hard_links_amount = os.stat(path).st_nlink

    return str(hard_links_amount)


def user_who_created(path: str) -> str:
    username = getpwuid(os.stat(path).st_uid).pw_name

    return username


def get_group(path: str) -> str:
    stat_info = os.stat(path)

    gid = stat_info.st_gid
    group = getgrgid(gid)[0]

    return group


def get_size(path: str) -> int:
    return os.path.getsize(path)


def get_date(path: str) -> str:
    unix_time = os.path.getsize(path)
    common_date = datetime.utcfromtimestamp(unix_time).strftime('%m-%d')

    return common_date


def get_time(path: str) -> str:
    unix_time = os.path.getsize(path)
    common_time = datetime.utcfromtimestamp(unix_time).strftime('%H:%M')

    return common_time
