#!/usr/bin/python

import csv
import sys


reader = csv.reader(sys.stdin, delimiter=',')
writer = csv.writer(sys.stdout, delimiter=',')

for line in reader:
    if len(line) > 0:
        this_key = line[0]
        arrival_delay = float(line[1])
        departure_delay = float(line[2])

        results = [this_key, arrival_delay, departure_delay]
        writer.writerow(results)
