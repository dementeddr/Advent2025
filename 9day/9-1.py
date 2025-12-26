#!/usr/bin/python3

import sys
import re
from time import perf_counter_ns

_day = 9 #Advent of Code day

## BEGIN SOLUTION

def main(data):

    coords = {}

    for i, line in enumerate(data):
        vals = tuple(map(int, line.split(",")))
        coords[i] = vals
        print(f"[{i}]={vals}")

    keys = range(len(data))
    largest = 0

    for i in keys[:-1]:
        for j in keys[i+1:]:
            area = calc_area(coords[i], coords[j])
            print(f"[{coords[i]} {coords[j]}]={area}")
            if area > largest:
                largest = area

    print(f"Largest Area = {largest}")


def calc_area(coord1, coord2):
    d1 = abs(coord1[0] - coord2[0])+1 
    d2 = abs(coord1[1] - coord2[1])+1 
    return d1 * d2

## END SOLUTION

if __name__ == "__main__":
    input_file = f"input-d{_day}.txt"
    lines = []

    if len(sys.argv) > 1:
        input_file = sys.argv[1]

    with open(input_file, "r", encoding="ascii") as fp:
        lines = list(map(lambda l: l[:-1], fp.readlines()))

    time_start = perf_counter_ns()
    main(lines)
    time_stop = perf_counter_ns()

    time = (time_stop - time_start) / 1000000
    print(f"\nExecution took {time:.4f} milliseconds")

