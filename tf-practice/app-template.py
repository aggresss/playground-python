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
    # print(FLAGS)
    a = tf.constant([1.0, 2.0], name="a")
    b = tf.constant([2.0, 3.0], name="b")
    result = a + b
    print(result)

    sess = tf.Session()
    with sess.as_default():
        print(result.eval())

    with tf.Session() as sess:
        print(sess.run(result))

    with tf.Session() as sess:
        print(result.eval(session=sess))


if __name__ == "__main__":
    tf.app.run()
