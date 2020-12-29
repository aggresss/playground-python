#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gdb


class ListNodePrinter(gdb.Command):
    """Prints the ListNode from our example in a nice format!"""
    def __init__(self):
        super(ListNodePrinter, self).__init__("walklist", gdb.COMMAND_USER)

    def invoke(self, args, from_tty):
        # You can pass args here so this routine could actually evaluate
        # different variables at runtime
        print("Args Passed: %s" % args)

        # Let's walk through the list starting with the head
        #
        # We can access value info by looking at:
        #  https://sourceware.org/gdb/onlinedocs/gdb/Values-From-Inferior.html#Values-From-Inferior
        node_ptr = gdb.parse_and_eval("s_list_head")

        count = 0
        while node_ptr != 0:
            print("%d: Addr: 0x%x, random value: %s" %
                  (count, node_ptr, int(node_ptr['random_value'])))
            node_ptr = node_ptr['next']
            count += 1
        print("Found %d nodes" % count)


ListNodePrinter()
