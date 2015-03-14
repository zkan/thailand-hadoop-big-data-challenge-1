#!/usr/bin/python

import csv
import sys


with open('data/origin_airports_with_delay.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')

    origin_airports_with_delay = []
    for line in reader:
        record = (line[0], float(line[1]), float(line[2]))
        origin_airports_with_delay.append(record)

    origin_airports_with_delay = sorted(
        origin_airports_with_delay,
        key=lambda x: x[1],
        reverse=True
    )

    origin_airport_list = '['
    avg_arrival_delay_list = '["Average Arrival Delay", '
    avg_departure_delay_list = '["Average Departure Delay", '
    for each in origin_airports_with_delay[:20]:
        origin_airport, avg_arrival_delay, avg_departure_delay = each
        avg_arrival_delay_list += '%s, ' % avg_arrival_delay
        avg_departure_delay_list += '%s, ' % avg_departure_delay
        origin_airport_list += '"%s", ' % origin_airport
    avg_arrival_delay_list += '],'
    avg_departure_delay_list += '],'
    origin_airport_list += ']'

    print origin_airport_list
    print avg_arrival_delay_list
    print avg_departure_delay_list
