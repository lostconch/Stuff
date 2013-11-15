#!/usr/bin/env python

from operator import itemgetter
import sys
import math

# Initialization
current_index = None
current_count = 0
current_sum = 0
current_sos = 0
index = None
value = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    index, value = line.split('\t', 1)

    # convert index (currently a string) to int and value to float
    try:
        index = int(index)
        value = float(value)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    # this if-else only works because Hadoop sorts map output
    # by key (here: index) before it is passed to the reducer
    if current_index == index:
        current_count += 1
        current_sum += value
        # Computing the sum of the squares
        current_sos += math.pow(value,2)
    else:
        if current_index:
            mean = current_sum/current_count
            # Computing the variance by subtracting the sum of the squares by the square of the mean
            variance = float(current_count)/(current_count-1)*(current_sos/current_count - math.pow(mean,2))
            # Output "current_index, current_count, mean, variance" every time a different index is reached
            print '%s,%s,%s,%s' % (current_index, current_count, mean, variance)
        current_count = 1
        current_index = index
        current_sum = value
        current_sos = math.pow(value,2)

# Output the last line of result!
if current_index == index:
    mean = current_sum/current_count
    variance = float(current_count)/(current_count-1)*(current_sos/current_count - math.pow(mean,2))
    print '%s,%s,%s,%s' % (current_index, current_count, mean, variance)

