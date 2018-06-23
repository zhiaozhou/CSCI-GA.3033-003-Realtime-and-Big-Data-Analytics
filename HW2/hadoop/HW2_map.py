#!/usr/bin/python

import os
import sys

terms = ['hackathon', 'Dec', 'Chicago', 'Java']

for line in sys.stdin:
    for term in terms:
        print("%s,%d" % (term,int(term.lower() in line.lower())))