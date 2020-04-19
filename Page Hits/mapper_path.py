#!/usr/bin/python

# Format of each line is:
# ip_addr, identity, username, time, zone, method, path, protocol, status,
# bytes of webpages 
#
# We want element 1 (path)
# We need to write them out to standard output, separated by a tab

import sys

for line in sys.stdin:
    data = line.strip().split(' ')
    if len(data) == 10:
        ipAddr, identity, username, time, zone, method, path, protocol, status, byteSize = data
        print "{0}".format(path.replace("http://www.the-associates.co.uk", ""))
