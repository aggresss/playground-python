#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

import os
import sys
import re
import math
import argparse
import numpy as np

from PIL import Image, ImageStat, ImageEnhance


# read file brightness value
def brightness(path):
    im = Image.open(path)
    stat = ImageStat.Stat(im)
    r, g, b = stat.mean
    return math.sqrt(0.241*(r**2) + 0.691*(g**2) + 0.068 * (b**2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog='debouncing.py',
        usage=' python %(prog)s -i input_path ',
        description='Make pictures debouncing.',
        epilog='SEE ALSO: http://github.com/aggresss/playground-python')

    parser.add_argument(
        '-i',
        '--ipath',
        type=str,
        default=None,
        help='picture path you want to debouncing')

    argvs = parser.parse_args()
    if argvs.ipath is None:
        print('please input picture fielpath')
        sys.exit(1)
    if argvs.ipath[-1] != os.path.sep:
        argvs.ipath = argvs.ipath + os.path.sep

    # find all image files
    im_list = []
    items = os.listdir(argvs.ipath)
    for item in items:
        if None is not re.match('(^\w+_\d+.jpg$)', item):
            if os.path.splitext(item)[1] == '.jpg':  # filter jpg files only
                im_list.append(item)

    # sort itmes by number index
    im_list.sort(key=lambda x: int(x.split('_')[1].split('.')[0]))

    # calculate fitness brightness curve
    bright_list = []
    for im in im_list:
        b = brightness(argvs.ipath + im)
        bright_list.append(b)

    im_index = []
    for item in im_list:
        im_index.append(int(item.split('_')[1].split('.')[0]))

    curve_poly = np.polyfit(im_index, bright_list, 10)
    curve_func = np.poly1d(curve_poly)
    fitting = curve_func(im_index)

    # Save fitness pictures
    for cnt, img in enumerate(im_list):
        im = Image.open(argvs.ipath + img)
        im = ImageEnhance.Brightness(im).enhance(
            fitting[cnt] / bright_list[cnt])
        im.save(argvs.ipath + img)

    sys.exit(0)
