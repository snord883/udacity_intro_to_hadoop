#!/usr/bin/python

import sys

count = 0
oldKey = None

# Loop around the data
# It will be in the format key\tval
# Where key is the request
#
# Counts for a particular request will be presented,
# then the key will change and we'll be dealing with the next store

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 1:
        # Something has gone wrong. Skip this line.
        continue

    thisKey = data_mapped

    if oldKey and oldKey != thisKey:
        print oldKey, "\t", count
        oldKey = thisKey
        count = 0

    oldKey = thisKey
    count += 1

if oldKey != None:
    print oldKey, "\t", count
