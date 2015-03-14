#!/usr/bin/python

import csv
import sys


reader = csv.reader(sys.stdin, delimiter=',')
writer = csv.writer(sys.stdout, delimiter=',')

for line in reader:
    # Skip the first line
    if line[0] == 'Year':
        continue

    origin = line[16]
    destination = line[17]
    distance = line[18]

    record = [origin, destination, distance]
    writer.writerow(record)
