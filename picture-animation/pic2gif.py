#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import sys
import os
import datetime
import imageio
import argparse


def create_gif(filenames, duration):
    print("Start to compose the gif file, please wait........")
    images = []
    for filename in filenames:
        images.append(imageio.imread(filename))
    output_file = 'Gif-%s.gif' % datetime.datetime.now().strftime(
        '%Y-%M-%d-%H-%M-%S')
    imageio.mimsave(output_file, images, duration=duration)
    print("Success to compose the gif file: %s" % (output_file))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog='pic2gif.py',
        usage=' python %(prog)s -p pictrue_path -d duration',
        description='Make pictures a gif file.',
        epilog='SEE ALSO: http://github.com/aggresss/playground-python')

    parser.add_argument(
        '-i',
        '--ipath',
        type=str,
        default=None,
        help='picture path you want to collect')
    parser.add_argument(
        '-d',
        '--duration',
        type=float,
        default=0.0,
        help='the duration of each picture')

    argvs = parser.parse_args()
    if argvs.ipath is None:
        print('please input picture fielpath')
        sys.exit()
    if argvs.ipath[-1] != os.path.sep:
        argvs.ipath = argvs.ipath + os.path.sep

    if argvs.duration == 0.0:
        print('please input the gif duration')
        sys.exit()

    filenames = []
    count = 0
    for img in os.listdir(argvs.ipath):
        filenames.append(argvs.ipath + img)
        print(argvs.ipath + img)
        count += 1

    VALID_EXTENSIONS = ('png', 'jpg')
    if not all(f.lower().endswith(VALID_EXTENSIONS) for f in filenames):
        print('Only png and jpg files allowed')
        sys.exit(1)

    print('\n' + 'Load %d file to create gif file........' % (count))
    create_gif(filenames, argvs.duration)
