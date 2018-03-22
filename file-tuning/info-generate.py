#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import sys, os
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog='info-generate.py',
        usage=' python %(prog)s -p path -s "suffix"',
        description='Generate list for files in one path.',
        epilog='SEE ALSO: http://github.com/aggresss/playground-python')

    parser.add_argument(
        '-p',
        '--path',
        type=str,
        default=None,
        help='file path you want to list')
    parser.add_argument(
        '-s',
        '--suffix',
        type=str,
        default='',
        help='suffix you want to add the list each line')
 
    argvs = parser.parse_args()
    if argvs.path == None:
        print('please input fielpath')
        sys.exit()
    # if argvs.path[-1] != os.path.sep:
    #     argvs.path = argvs.path + os.path.sep
    with open(argvs.path + '.txt', 'w') as f:
        for img in os.listdir(argvs.path):
            line = argvs.path + os.path.sep + img+ argvs.suffix +'\n'
            f.write(line)

# EOF