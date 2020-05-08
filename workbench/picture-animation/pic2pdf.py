#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

import sys
import os
import datetime
import argparse
from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfgen import canvas


def create_pdf(filenames, isLandscape):
    print("Start to compose the pdf file, please wait........")
    output_file = 'pdf-%s.pdf' % datetime.datetime.now().strftime(
        '%Y-%M-%d-%H-%M-%S')

    if isLandscape is True:
        (w, h) = landscape(A4)
        c = canvas.Canvas(output_file, pagesize=landscape(A4))
    else:
        (w, h) = A4
        c = canvas.Canvas(output_file, pagesize=A4)

    for filename in filenames:
        c.drawImage(filename, 0, 0, w, h)
        c.showPage()
    c.save()

    print("Success to compose the pdf file: %s" % (output_file))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog='pic2pdf.py',
        usage=' python %(prog)s -i pictrue_path -l landscope',
        description='Make pictures to a pdf file.',
        epilog='SEE ALSO: http://github.com/aggresss/playground-python')

    parser.add_argument(
        '-i',
        '--ipath',
        type=str,
        default=None,
        help='picture path you want to collect')
    parser.add_argument(
        '-l',
        '--landscope',
        type=bool,
        default=False,
        help='need landscope')

    argvs = parser.parse_args()
    if argvs.ipath is None:
        print('please input picture fielpath')
        sys.exit()
    if argvs.ipath[-1] != os.path.sep:
        argvs.ipath = argvs.ipath + os.path.sep

    filenames = []
    count = 0
    for img in os.listdir(argvs.ipath):
        filenames.append(argvs.ipath + img)
        print(argvs.ipath + img)
        count += 1
    filenames.sort()

    VALID_EXTENSIONS = ('png', 'jpg')
    if not all(f.lower().endswith(VALID_EXTENSIONS) for f in filenames):
        print('Only png and jpg files allowed')
        sys.exit(1)

    print('\n' + 'Load %d file to create pdf file........' % (count))
    create_pdf(filenames, argvs.landscope)
