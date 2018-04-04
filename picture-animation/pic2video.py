#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
OpenCV CV_FOURCC type
CV_FOURCC('P', 'I', 'M', '1') = MPEG-1 codec
CV_FOURCC('M', 'J', 'P', 'G') = motion-jpeg codec
CV_FOURCC('M', 'P', '4', '2') = MPEG-4.2 codec
CV_FOURCC('D', 'I', 'V', '3') = MPEG-4.3 codec
CV_FOURCC('D', 'I', 'V', 'X') = MPEG-4 codec
CV_FOURCC('U', '2', '6', '3') = H263 codec
CV_FOURCC('I', '2', '6', '3') = H263I codec
CV_FOURCC('F', 'L', 'V', '1') = FLV1 codec

"""

from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

import sys
import os
import datetime
import cv2
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog='pic2video.py',
        usage=' python %(prog)s -p pictrue_path -f fps',
        description='Make pictures to video file.',
        epilog='SEE ALSO: http://github.com/aggresss/playground-python')

    parser.add_argument(
        '-i',
        '--ipath',
        type=str,
        default=None,
        help='picture path you want to collect')
    parser.add_argument(
        '-f',
        '--fps',
        type=float,
        default=15.0,
        help='the FPS of each video')

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
        count += 1
    filenames.sort()
    # filenames.sort(key=lambda x: int(x[-12:-4]))
    for item in filenames:
        print(item)

    VALID_EXTENSIONS = ('png', 'jpg')
    if not all(f.lower().endswith(VALID_EXTENSIONS) for f in filenames):
        print('Only png and jpg files allowed')
        sys.exit(1)

    print('\n' + 'Load %d files to create video file........' % (count))

    print("Start to compose the video file, please wait........")
    output_file = 'video-%s.mp4' % datetime.datetime.now().strftime(
        '%Y-%M-%d-%H-%M-%S')
    fourcc = cv2.VideoWriter_fourcc(*'DIVX')
    # videoWriter = cv2.VideoWriter(output_file, fourcc, argvs.fps, (960, 544))
    videoWriter = cv2.VideoWriter(output_file, fourcc, argvs.fps, (640, 368))
    for filename in filenames:
        img = cv2.imread(filename)
        frame = cv2.resize(img, (640, 368))
        videoWriter.write(frame)
    videoWriter.release()

    print("Success to compose the mp4 file: %s" % (output_file))
