#!/usr/bin/python

import csv
import sys


reader = csv.reader(sys.stdin, delimiter=',')
writer = csv.writer(sys.stdout, delimiter=',')

old_key = None

for line in reader:
    if len(line) > 0:
        this_key = line[0]
        distance = line[1]

        if old_key and old_key != this_key:
            origin, destination = old_key.split('-')
            results = [origin, destination, distance]
            writer.writerow(results)

        old_key = this_key


if old_key != None:
    origin, destination = old_key.split('-')
    results = [origin, destination, distance]
    writer.writerow(results)
