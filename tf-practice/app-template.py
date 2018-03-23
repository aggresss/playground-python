#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf

flags = tf.flags
logging = tf.logging

flags.DEFINE_string(
    'filename', '',
    'File (Image) or File list (Text/No header TSV) to process')

# flags.DEFINE_bool("para_name_2", "default_val", "description")
FLAGS = flags.FLAGS


def main(_):
    FLAGS.filename


if __name__ == "__main__":
    tf.app.run()
