#!/usr/bin/python3

import sys
import re
from time import perf_counter_ns

_day = 5 #Advent of Code day

## BEGIN SOLUTION

def main(data):

    ranges = []

    for i, line in enumerate(data):
        if len(line) == 0:
            read_ingredients = True
            break

        rng = tuple(map(int,line.split('-')))
        start = (True, rng[0], i)
        end = (False, rng[1], i)
        ranges.append(start)
        ranges.append(end)

    ranges.sort(key=lambda r: (r[1], not r[0]))
    open_ranges = []
    count = 0

    first_start = 0

    for endpoint in ranges:
        if endpoint[0]:
            open_ranges.append(endpoint[2])
        else:
            open_ranges.remove(endpoint[2])

        suffix = ""

        if len(open_ranges) == 1 and endpoint[0]:
            first_start = endpoint[1]
            suffix = "Starting range."

        elif len(open_ranges) == 0:
            range_size = endpoint[1] - first_start + 1
            count += range_size
            suffix = f"Ending range {first_start}-{endpoint[1]}. Add {range_size}. Total {count}\n"

        print(f"{endpoint} {len(open_ranges)} {suffix}")

    print(f"Total size of fresh ingredient ranges: {count}")

    
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

