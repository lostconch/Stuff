#!/usr/bin/env python

import sys
import math

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into numbers
    numbers = line.split()

    if line:
        array = [i for i in numbers]
        
        # Compute x_lo, x_hi, y_lo, and y_hi
        x_lo = math.floor(float(array[0])*10)/10
        x_hi = math.ceil(float(array[0])*10)/10
        y_lo = math.floor(float(array[1])*10)/10
        y_hi = math.ceil(float(array[1])*10)/10
        
        # Write "x_lo, x_hi, y_lo, y_hi, count" as a <key,value> pair to STDOUT, used as the input of the reducer later
        print '%s,%s,%s,%s\t%s' % (x_lo, x_hi, y_lo, y_hi, 1)
