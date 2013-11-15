#!/usr/bin/env python

from operator import itemgetter
import sys

current_bin = None
current_count = 0
bin = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    bin, count = line.split('\t', 1)

    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    # this if-else only works because Hadoop sorts map output
    # by key (here: bin) before it is passed to the reducer
    if current_bin == bin:
        current_count += count
    else:
        if current_bin:
            # Output "x_lo, x_hi, y_lo, y_hi, count" every time a different bin is reached
            print '%s,%s' % (current_bin, current_count)
        current_count = count
        current_bin = bin

# Output the last line of result
if current_bin == bin:
    print '%s,%s' % (current_bin, current_count)
    
