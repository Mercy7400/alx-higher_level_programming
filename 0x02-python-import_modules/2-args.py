#!/usr/bin/python3

import sys

if len(sys.argv) == 1:
    print("{} argument(s)".format(len(sys.argv) - 1), end=".")
else:
    print("{} argument(s):".format(len(sys.argv) - 1))

for i, arg in enumerate(sys.argv[1:]):
    print("{}: {}".format(i + 1, arg))
