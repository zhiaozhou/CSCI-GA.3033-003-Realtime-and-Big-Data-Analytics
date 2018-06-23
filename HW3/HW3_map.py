#!/usr/bin/python

import os
import sys

for line in sys.stdin:
    elem = line.strip().split(' ')
    for i in elem[1:-1]:
        print("%s %s %.6f" % (i,elem[0],float(elem[-1])/len(elem[1:-1])))