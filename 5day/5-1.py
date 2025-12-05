#!/usr/bin/python3

import sys
import re
from time import perf_counter_ns

_day = 5 #Advent of Code day

## BEGIN SOLUTION

def main(data):

    read_ingredients = False
    ranges = []
    count = 0

    for line in data:
        if len(line) == 0:
            read_ingredients = True
            continue

        if not read_ingredients:
            ranges.append(tuple(map(int,line.split('-'))))
        else:
            ingredient = int(line)

            for rng in ranges:
                if rng[0] <= ingredient <= rng[1]:
                    count += 1
                    break
    print(f"Available ingredients: {count}")

    
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

