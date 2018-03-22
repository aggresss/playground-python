#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import division

import os
import sys
import argparse
import cv2

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog='video2pic.py',
        usage=' python %(prog)s -p path -v video -o output_path ',
        description='Capture video to picture.',
        epilog='SEE ALSO: http://github.com/aggresss/playground-python')

    parser.add_argument(
        '-v',
        '--video',
        type=str,
        default=None,
        help='video path you want to cap')
    parser.add_argument(
        '-o',
        '--opath',
        type=str,
        default=None,
        help='output path of the pictrue cap from video')

    argvs = parser.parse_args()
    if argvs.video is None:
        print('please input video fielpath')
        sys.exit()

    if argvs.opath is None:
        print('please input the output path')
        sys.exit()
    elif os.path.exists(argvs.opath) is False:
        os.makedirs(argvs.opath)
    if argvs.opath[-1] != os.path.sep:
        argvs.opath = argvs.opath + os.path.sep

    vidcap = cv2.VideoCapture(argvs.video)
    fps = vidcap.get(cv2.CAP_PROP_FPS)
    size = (int(vidcap.get(cv2.CAP_PROP_FRAME_WIDTH)),
            int(vidcap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    sum_frame = vidcap.get(cv2.CAP_PROP_FRAME_COUNT)
    sum_time = float(sum_frame) / float(fps)

    count = 1
    success = True
    success, image = vidcap.read()
    while success:
        cv2.imwrite(argvs.opath + "frame_%d.jpg" % count, image)
        print("output file: " + argvs.opath + "frame_%d.jpg" % count)
        success, image = vidcap.read()
        count += 1

    print("The video FPS is: %d" % (fps))
    print("The video frame size is: %dX%d" % (size))
    print("The video frame number is %d" % (sum_frame))
    print("The video time length is %.3f second." % (sum_time))
