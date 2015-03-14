#!/usr/bin/python

import csv
import sys


reader = csv.reader(sys.stdin, delimiter=',')
writer = csv.writer(sys.stdout, delimiter=',')

top_five_airlines = ['WN', 'AA', 'OO', 'MQ', 'US']

for line in reader:
    # Skip the first line
    if line[0] == 'Year':
        continue

    carrier_id = line[8]
    if carrier_id not in top_five_airlines:
        continue

    month = '%02d' % int(line[1])

    key = carrier_id + '-' + month
    arrival_delay = line[14]

    record = [key, arrival_delay]
    writer.writerow(record)
