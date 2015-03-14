#!/usr/bin/python

import csv
import sys


reader = csv.reader(sys.stdin, delimiter=',')
writer = csv.writer(sys.stdout, delimiter=',')

old_key = None
total_arrival_delay = 0
count = 0

for line in reader:
    if len(line) > 0:
        this_key = line[0]
        arrival_delay = float(line[1])

        if old_key and old_key != this_key:
            avg_arrival_delay = total_arrival_delay / count
            results = [old_key, avg_arrival_delay]
            writer.writerow(results)

            total_arrival_delay = 0
            count = 0

        old_key = this_key
        total_arrival_delay += arrival_delay
        count += 1


if old_key != None:
    avg_arrival_delay = total_arrival_delay / count
    results = [old_key, avg_arrival_delay]
    writer.writerow(results)
