#!/usr/bin/python

import sys

count = 0
node_list = []

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) > 2:
        #Something has gone wrong. Skip this line.
        continue
    elif len(data_mapped) == 2:
        node_list.append(int(data_mapped[0]))
    else:
        count += float(data_mapped[0])

node_list.sort()
print("{0}\t{1}").fotmat(count, node_list)