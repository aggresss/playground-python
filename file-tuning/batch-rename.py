#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import sys
import os
import argparse
import random

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog='batch-rename.py',
        usage=' python -m %(prog)s --path xxxx --prefix yyyy',
        description='Batch rename files under specified folder.',
        epilog='SEE ALSO: http://github.com/aggresss/playground-python')

    parser.add_argument(
        '-p',
        '--path',
        type=str,
        default=None,
        help='file path you want to rename')
    parser.add_argument(
        '-f',
        '--prefix',
        type=str,
        default=str(random.randint(1000, 9999)),
        help='filename prefix')
    args = parser.parse_args()
    if args.path is None:
        print('please input fielpath')
        sys.exit()
    if args.path[-1] != os.path.sep:
        args.path = args.path + os.path.sep

    file_list = os.listdir(args.path)
    n = 0
    for i in file_list:
        oldname = args.path + file_list[n]
        file_ext = os.path.splitext(file_list[n])[1]
        newname = args.path + args.prefix + '_' + str(n + 1) + file_ext
        os.rename(oldname, newname)
        print(oldname, ' ======> ', newname)
        n += 1
