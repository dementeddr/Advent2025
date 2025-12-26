#!/usr/bin/python3

import sys
import re
import math
from time import perf_counter_ns

_day = 8 #Advent of Code day

## BEGIN SOLUTION

def main(data, iterations):

    coords = {}
    distances = {}
    circuits = []

    for i, line in enumerate(data):
        vals = tuple(map(int, line.split(",")))
        coords[i] = vals
        #print(f"[{i}]={vals}")

    keys = range(len(data))

    for i in keys[:-1]:
        for j in keys[i+1:]:
            dist = calc_dist(coords[i], coords[j])
            tup = (i,j)
            distances[tup] = dist

    kvps = sorted(distances.items(), key=lambda kvp: kvp[1])
    
    #for kvp in kvps:
    #    print(f"{kvp[0]}={kvp[1]}")

    for i in range(iterations):
        link = kvps.pop(0)
        boxes = link[0]
        add_link(circuits, boxes)
        #print(circuits)

    sizes = sorted(list(map(len, circuits)), reverse=True)
    print(f"{sizes=}")
    total = sizes[0] * sizes[1] * sizes[2]
    print(f"Circuit math says {total}")


def add_link(circuits, boxes):

    found = []

    for circ in circuits:
        if boxes[0] in circ and boxes[1] in circ:
            return
        if boxes[0] in circ or boxes[1] in circ:
            found.append(circ)

    if len(found) == 0:
        new_circ = {boxes[0], boxes[1]}
        circuits.append(new_circ)
    elif len(found) == 1:
        found[0].add(boxes[0])
        found[0].add(boxes[1])
    elif len(found) == 2:
        found[0].add(boxes[0])
        found[0].add(boxes[1])
        found[0] |= found[1]
        circuits.remove(found[1])
    else:
        sys.exit(1)
        

def calc_dist(coord1, coord2):
    d1 = coord1[0] - coord2[0]
    d2 = coord1[1] - coord2[1]
    d3 = coord1[2] - coord2[2]
    return math.sqrt(d1**2 + d2**2 + d3**2)

    
## END SOLUTION

if __name__ == "__main__":
    input_file = f"input-d{_day}.txt"
    iterations = 1000
    lines = []

    if len(sys.argv) > 1:
        iterations = int(sys.argv[1])
    if len(sys.argv) > 2:
        input_file = sys.argv[2]

    with open(input_file, "r", encoding="ascii") as fp:
        lines = list(map(lambda l: l[:-1], fp.readlines()))

    time_start = perf_counter_ns()
    main(lines, iterations)
    time_stop = perf_counter_ns()

    time = (time_stop - time_start) / 1000000
    print(f"\nExecution took {time:.4f} milliseconds")

