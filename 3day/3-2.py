#!/usr/bin/python3

import sys
import re
from time import perf_counter_ns

_day = 3 #Advent of Code day

## BEGIN SOLUTION

def main(data):

    total = 0

    for line in data:
        digits = list(map(int, line[:-1]))
        batts = []
        indices = []
        last_index = -1
        for i in reversed(range(12)):
            index = find_high(digits[last_index+1:len(digits)-i]) + last_index + 1
            last_index = index
            indices.append(index)
            batts.append(digits[index])

        joltage = int("".join(map(str,batts)))
        total += joltage
        print(f"{line[:-1]}  {indices}   {joltage}  {total}")
        
    print(f"Total Joltage: {total}")


def find_high(digits):
    #print(f"{digits}")
    hi_idx = 0
    for i, digit in enumerate(digits):
        if digit > digits[hi_idx]:
            hi_idx = i
    return hi_idx

    
## END SOLUTION

if __name__ == "__main__":
    input_file = f"input-d{_day}.txt"
    data = []

    if len(sys.argv) > 1:
        input_file = sys.argv[1]

    with open(input_file, "r", encoding="ascii") as fp:
        data = fp.readlines()

    time_start = perf_counter_ns()
    main(data)
    time_stop = perf_counter_ns()

    time = (time_stop - time_start) / 1000000
    print(f"\nExecution took {time:.4f} milliseconds")

