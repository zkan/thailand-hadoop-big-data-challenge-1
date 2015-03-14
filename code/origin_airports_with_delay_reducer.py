#!/usr/bin/python

import csv
import sys


reader = csv.reader(sys.stdin, delimiter=',')
writer = csv.writer(sys.stdout, delimiter=',')

old_key = None
total_arrival_delay = 0
total_departure_delay = 0
count = 0

for line in reader:
    if len(line) > 0:
        this_key = line[0]
        arrival_delay = float(line[1])
        departure_delay = float(line[2])

        if old_key and old_key != this_key:
            avg_arrival_delay = total_arrival_delay / count
            avg_departure_delay = total_departure_delay / count

            if avg_arrival_delay < 0:
                avg_arrival_delay = 0
            if avg_departure_delay < 0:
                avg_departure_delay = 0

            results = [old_key, avg_arrival_delay, avg_departure_delay]
            writer.writerow(results)

            total_arrival_delay = 0
            total_departure_delay = 0
            count = 0

        old_key = this_key
        total_arrival_delay += arrival_delay
        total_departure_delay += departure_delay
        count += 1


if old_key != None:
    if avg_arrival_delay < 0:
        avg_arrival_delay = 0
    if avg_departure_delay < 0:
        avg_departure_delay = 0

    avg_arrival_delay = total_arrival_delay / count
    avg_departure_delay = total_departure_delay / count
    results = [old_key, avg_arrival_delay, avg_departure_delay]
    writer.writerow(results)
