#!/usr/bin/python

import csv
import sys


reader = csv.reader(sys.stdin, delimiter=',')
writer = csv.writer(sys.stdout, delimiter=',')

for line in reader:
    # Skip the first line
    if line[0] == 'Year':
        continue

    weather_delay = line[25]
    arrival_delay = line[14]
    departure_delay = line[15]

    if weather_delay == 'NA' or weather_delay == '0':
        continue

    if arrival_delay == 'NA':
        continue

    if departure_delay == 'NA':
        continue

    record = [weather_delay, arrival_delay, departure_delay]
    writer.writerow(record)
