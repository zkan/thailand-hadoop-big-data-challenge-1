#!/usr/bin/python

import csv
import sys


with open('data/weather_causing_delay.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')

    weather_casuing_delay_list = []
    for line in reader:
        record = (int(line[0]), float(line[1]), float(line[2]))
        weather_casuing_delay_list.append(record)

    weather_casuing_delay_list = sorted(weather_casuing_delay_list)

    weather_delay_list = '["Weather Delay", '
    avg_arrival_delay_list = '["Average Arrival Delay", '
    avg_departure_delay_list = '["Average Departure Delay", '
    for each in weather_casuing_delay_list:
        weather_delay, avg_arrival_delay, avg_departure_delay = each
        weather_delay_list += '%s, ' % weather_delay
        avg_arrival_delay_list += '%s, ' % avg_arrival_delay
        avg_departure_delay_list += '%s, ' % avg_departure_delay
    weather_delay_list += '],'
    avg_arrival_delay_list += '],'
    avg_departure_delay_list += '],'

    print weather_delay_list
    print avg_arrival_delay_list
    print avg_departure_delay_list
