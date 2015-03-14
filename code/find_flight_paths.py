#!/usr/bin/python

import csv
import sys


# Credit: https://www.python.org/doc/essays/graphs/
def find_shortest_path(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if not graph.has_key(start):
            return None
        shortest = None
        for node in graph[start]:
            if node not in path:
                newpath = find_shortest_path(graph, node, end, path)
                if newpath:
                    if not shortest or len(newpath) < len(shortest):
                        shortest = newpath
        return shortest


# Credit: https://www.python.org/doc/essays/graphs/
def find_all_paths(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if not graph.has_key(start):
            return []
        paths = []
        for node in graph[start]:
            if node not in path:
                newpaths = find_all_paths(graph, node, end, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths


# Credit: https://www.python.org/doc/essays/graphs/
def find_path(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if not graph.has_key(start):
            return None
        for node in graph[start]:
            if node not in path:
                newpath = find_path(graph, node, end, path)
                if newpath: return newpath
        return None


with open('data/origin_to_destination.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')

    graph = {}
    for line in reader:
        origin = line[0]
        destination = line[1]

        if origin not in graph:
            graph[origin] = [destination]
        else:
            graph[origin].append(destination)

    print find_path(graph, 'ATW', 'HNL')
