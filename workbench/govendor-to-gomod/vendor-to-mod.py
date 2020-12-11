#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import argparse
import json
from datetime import datetime

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog='vendor-to-mod.py',
        usage='python %(prog)s \
-v vendor_json_file \
-m go_mod_file \
-r replace_prefix',
        description='Convert vendor.json file to go.mod',
        epilog='SEE ALSO: http://github.com/aggresss/playground-python')

    parser.add_argument(
        '-v',
        '--vfile',
        type=str,
        default=None,
        help='vendor.json file you want to convert')
    parser.add_argument(
        '-m',
        '--mfile',
        type=str,
        default=None,
        help='go.mod file you want to append')
    parser.add_argument(
        '-r',
        '--replace',
        type=str,
        default=None,
        help='replece prefix if you want to replace')

    argvs = parser.parse_args()

    if argvs.vfile is None:
        print('please input vendor.json file path')
        sys.exit()

    if argvs.mfile is None:
        print('please input go.mod file path')
        sys.exit()

    with open(argvs.vfile, 'r') as vendor_file:
        vendor_dict = json.load(vendor_file)
        print(len(vendor_dict['package']))

    if len(vendor_dict['package']) > 0:
        with open(argvs.mfile, 'a') as mod_file:
            mod_file.write("""
require(
""")
            for index, element in enumerate(vendor_dict['package']):
                # module path
                mod_file.write('\t' + element['path'] + ' ')
                # assemble version-date-revision
                # 1. version
                if 'version' in element and element['version'] != '':
                    v_index = element['version'].find('v')
                    mod_file.write(element['version'][v_index:])
                else:
                    mod_file.write('v0.0.0')
                # 2. date
                if 'revisionTime' in element and element['revisionTime'] != '':
                    utc_time = datetime.strptime(
                        element['revisionTime'],
                        '%Y-%m-%dT%H:%M:%SZ')
                    mod_file.write('-' + utc_time.strftime('%Y%m%d%H%M%S'))
                else:
                    mod_file.write('-197001010000')
                # 3. revision
                if 'revision' in element and element['revision'] != '':
                    mod_file.write('-' + element['revision'][0:12])
                else:
                    mod_file.write('-000000000000')
                # EOL
                mod_file.write('\n')

            mod_file.write(')\n')
