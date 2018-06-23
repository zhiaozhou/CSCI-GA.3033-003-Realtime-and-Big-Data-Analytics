#!/usr/bin/python

import sys
from collections import defaultdict

output = defaultdict(int)
for line in sys.stdin:
    key = line.split(",")[0]
    value = int(line.split(",")[1])
    output[key] += value
for i,j in output.items():
    print("%s %d" % (i,j))