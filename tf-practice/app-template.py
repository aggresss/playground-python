#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf

tf.flags.DEFINE_string('filename', 'this is default string.', 'File Name')
tf.flags.DEFINE_integer('filenum', 1024, 'File number')
tf.flags.DEFINE_bool('filebool', True, "description bool")
FLAGS = tf.flags.FLAGS


def main(_):
    print(FLAGS)


if __name__ == "__main__":
    tf.app.run()
