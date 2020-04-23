#!/usr/bin/python

# Format of each line is:
# node_id, title, tagnames, author_id, body, node_type, parent_id, abs_parent_id, added_at,
# score, state_string, last_edit_id, last_activity_by_id, last_activity_at, active_revision_id,
# extra, extra_ref_id, extra_count, mark
# 
# Used the try/catch, because I was running into an issue with csv.Error: newLine in String
# on certain lines

import sys
import re
import csv

reader = csv.reader(sys.stdin, delimiter='\t', quoting=csv.QUOTE_ALL, quotechar='"')

while True:
    try:
        data = reader.next()
        if len(data) == 19:
            word_list = re.findall("[\w]+",data[4])
            fantastic_list = [w for w in word_list if str.lower(w)=="fantastic"]
            fantastically_list = [w for w in word_list if str.lower(w)=="fantastically"]
            if len(fantastic_list) > 0:
                print('{0}').format(len(fantastic_list))
            if len(fantastically_list) > 0:
                print('{0}\t{1}').format(data[0], len(fantastically_list))
    except csv.Error:
        continue
    except StopIteration:
        break