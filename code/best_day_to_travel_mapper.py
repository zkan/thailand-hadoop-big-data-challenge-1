#!/usr/bin/python

import csv
import sys


reader = csv.reader(sys.stdin, delimiter=',')
writer = csv.writer(sys.stdout, delimiter=',')

for line in reader:
    # Skip the first line
    if line[0] == 'Year':
        continue

    day_of_week = line[3]
    arrival_delay = line[14]
    departure_delay = line[15]

    if arrival_delay == 'NA':
        continue

    if departure_delay == 'NA':
        continue

    record = [day_of_week, arrival_delay, departure_delay]
    writer.writerow(record)
