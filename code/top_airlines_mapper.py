#!/usr/bin/python

import csv
import sys


reader = csv.reader(sys.stdin, delimiter=',')
writer = csv.writer(sys.stdout, delimiter=',')

for line in reader:
    # Skip the first line
    if line[0] == 'Year':
        continue

    carrier_id = line[8]

    record = [carrier_id]
    writer.writerow(record)
