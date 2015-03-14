#!/usr/bin/python

import csv
import sys


with open('data/arrival_delay_results.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')

    old_key = None
    data = ''

    for line in reader:
        this_key, month = line[0].split('-')
        arrival_delay = line[1]

        if old_key and old_key != this_key:
            results = '["%s", ' % old_key
            results += data + '],'

            print results

            data = ''

        old_key = this_key
        data += '%s, ' % arrival_delay

if old_key != None:
    results = '["%s", ' % old_key
    results += data + ']'

    print results
