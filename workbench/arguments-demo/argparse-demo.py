#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog='argparse-demo.py',
        usage='%(prog)s [options] usage',
        description='demo - description',
        epilog='demo - epilog')

    # option arguments
    parser.add_argument(
        '-v',
        '--version',
        action='version',
        version='version demo',
        help='Show program version info and exit.')
    parser.add_argument('-f', '--foo', type=int, default=64)
    parser.add_argument('-s', '--string', type=str, default=None)
    parser.add_argument('-x', '--xxx', dest='yyy', type=int, default=128)

    # required arguments
    parser.add_argument('require_str', type=str)
    parser.add_argument('require_int', type=int)

    args = parser.parse_args()
    print(args)
