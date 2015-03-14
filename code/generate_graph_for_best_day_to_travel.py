#!/usr/bin/python

import csv
import sys


with open('data/best_day_to_travel.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')

    avg_arrival_delay_list = '["Average Arrival Delay", '
    avg_departure_delay_list = '["Average Departure Delay", '
    for line in reader:
        day_of_week, avg_arrival_delay, avg_departure_delay = line
        avg_arrival_delay_list += '%s, ' % avg_arrival_delay
        avg_departure_delay_list += '%s, ' % avg_departure_delay
    avg_arrival_delay_list += '],'
    avg_departure_delay_list += '],'

    print avg_arrival_delay_list
    print avg_departure_delay_list
