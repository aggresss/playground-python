#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import argparse
import json

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog='vendor-to-mod.py',
        usage='python %(prog)s \
-v vendor_json_file \
-m go_mod_file \
-r replace_prefix',
        description='Convert vendor.json file to go.mod',
        epilog='SEE ALSO: http://github.com/aggresss/playground-python')

    parser.add_argument(
        '-v',
        '--vfile',
        type=str,
        default=None,
        help='vendor.json file you want to convert')
    parser.add_argument(
        '-m',
        '--mfile',
        type=str,
        default=None,
        help='go.mod file you want to append')
    parser.add_argument(
        '-r',
        '--replace',
        type=str,
        default=None,
        help='replece prefix if you want to replace')

    argvs = parser.parse_args()

    if argvs.vpath is None:
        print('please input vendor.json file path')
        sys.exit()

    if argvs.mpath is None:
        print('please input go.mod file path')
        sys.exit()
