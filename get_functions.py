#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from stat import filemode
from pwd import getpwuid
from grp import getgrgid

from datetime import datetime


def get_chmod(path: str) -> str:
    file_status = os.lstat(path)
    chmod = filemode(file_status.st_mode)

    return chmod


def get_hard_links_amount(path: str) -> str:
    hard_links_amount = os.lstat(path).st_nlink
    
    return str(hard_links_amount)


def user_who_created(path: str) -> str:
    username = getpwuid(os.lstat(path).st_uid).pw_name

    return username


def get_uid(path: str) -> str:
    uid = getpwuid(os.lstat(path).st_uid).pw_uid

    return uid


def get_group(path: str) -> str:
    stat_info = os.lstat(path)

    gid = stat_info.st_gid
    group = getgrgid(gid)[0]

    return group


def get_gid(path: str) -> str:
    gid = getgrgid(os.lstat(path).st_gid).gr_gid

    return gid


def get_size(path: str) -> str:
    # size = str(os.path.getsize(path))
    size = str(os.lstat(path).st_size)
    return size


def get_date(path: str) -> str:
    unix_time = os.lstat(path).st_mtime
    common_date = datetime.utcfromtimestamp(unix_time).strftime('%m-%d')

    return common_date


def get_time(path: str) -> str:
    unix_time = os.lstat(path).st_mtime + 3600
    common_time = datetime.utcfromtimestamp(unix_time).strftime('%H:%M')

    return common_time
