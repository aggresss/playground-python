#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

print "file = ", sys.argv[0]
for i in range(1, len(sys.argv)):
    print "parameter%s = %s" % (i, sys.argv[i])
