#!/usr/bin/env python

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into numbers
    numbers = line.split()

    if line:
        array = [i for i in numbers]
        # Read in the index and the value for each line
        index = array[0]
        value = array[1]
        # Write "index, value" as a <key,value> pair to STDOUT, used as the input of the reducer later
        print '%s\t%s' % (index, value)
