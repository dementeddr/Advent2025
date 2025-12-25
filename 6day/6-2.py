#!/usr/bin/python3

import sys
import re
from time import perf_counter_ns
from collections import defaultdict
from functools import reduce

_day = 6 #Advent of Code day

## BEGIN SOLUTION

def main(data):

    total = 0
    nums = []

    for x in reversed(range(len(data[0]))):
        num = ''
        for y in range(len(data) - 1):
            num += data[y][x]

        if num.isspace():
            continue

        nums.append(int(num))
        opc = data[-1][x]

        if opc != ' ':
            sol = perform(nums, opc)
            total += sol
            print(f"{opc}({nums}) = {sol}  -> {total}")
            nums = []

    # MAKE NEW FILE!


    print(f"Total of all solutions = {total}")



def perform(nums, opc):
    
    if opc == '*':
        return reduce(lambda a, b: a*b, nums)
    elif opc == '+':
        return reduce(lambda a, b: a+b, nums)
    else:
        return 0


    
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

