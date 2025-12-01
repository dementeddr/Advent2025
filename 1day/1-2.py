#!/usr/bin/python3

import sys
import re
from time import perf_counter_ns

_day = 1 #Advent of Code day

## BEGIN SOLUTION

def main(data):

    point = 50
    count = 0

    for line in data:
        turn = line[0]
        dist = int(line[1:])
        
        count += dist // 100
        remainder = dist % 100

        if turn == 'L':
            dist = -dist
            if remainder >= point and point != 0:
                count += 1
        elif remainder >= (100 - point):
            count += 1

        point = (point + dist) % 100

        print(f"{line[:-1]} -> {dist} = {point}, c {count}")

    print(f"\nZero-point count = {count}")

    
## END SOLUTION

if __name__ == "__main__":
    input_file = f"input-d{_day}.txt"
    data = []

    if len(sys.argv) > 1:
        input_file = sys.argv[1]

    with open(input_file, "r") as fp:
        data = fp.readlines()

    time_start = perf_counter_ns()
    main(data)
    time_stop = perf_counter_ns()

    time = (time_stop - time_start) / 1000000
    print(f"\nExecution took {time:.4f} milliseconds")

