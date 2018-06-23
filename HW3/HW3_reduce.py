#!/usr/bin/python

import sys
from collections import defaultdict

result = defaultdict(lambda: [[],0])
original = []
for line in sys.stdin:
    result[line.split(' ')[0]][1] += float(line.split(' ')[-1])
    original.append(line)
for key in result.keys():
    result[key][0].append([line[0] for line in original if line.split(' ')[1]==key])
    
for i in result:
    print('%s %s %.6f' % (i, ' '.join(result[i][0][0]), result[i][-1]))