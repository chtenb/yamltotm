#!/usr/bin/env python3

"""
Convert tmTheme plist to YAML.

Reads a theme in tmTheme plist format used in TextMate and Sublime Text,
and outputs YAML format.

Note: Uses plistlib interface introduced in Python 3.4.
"""

import argparse
import plistlib
import yaml

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert tmTheme to YAML.')
    parser.add_argument('infile', type=argparse.FileType('rb'),
                        help='tmTheme theme file')
    parser.add_argument('outfile', type=argparse.FileType('w'),
                        help='YAML theme file')
    args = parser.parse_args()

    # read tmTheme plist and write YAML
    theme = plistlib.load(args.infile)
    yaml.safe_dump(theme, stream=args.outfile, default_flow_style=False)