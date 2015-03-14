#!/usr/bin/python

import csv
import sys


reader = csv.reader(sys.stdin, delimiter=',')
writer = csv.writer(sys.stdout, delimiter=',')

old_key = None
count = 0

for line in reader:
    if len(line) > 0:
        carrier_id = line[0]
        this_key = carrier_id

        if old_key and old_key != this_key:
            results = [old_key, count]
            writer.writerow(results)

            count = 0

        old_key = this_key
        count += 1


if old_key != None:
    results = [old_key, count]
    writer.writerow(results)
