#!/usr/bin/python3

import sys
import re
from time import perf_counter_ns
from collections import defaultdict

_day = 6 #Advent of Code day

## BEGIN SOLUTION

def main(data):

    problems = defaultdict(list)
    num_pat = re.compile(r"\d+")

    for line in data[:-1]:
        nums = list(map(int, num_pat.findall(line)))
        print(nums)
        for i, num in enumerate(nums):
            problems[i].append(num)

    ops = re.compile(r"\S+").findall(data[-1])
    print(ops)
    total = 0

    list(map(lambda x: print(f"[{x}] {problems[x]}"), problems))

    for i, op in enumerate(ops):
        solution = 0 if op == '+' else 1
        output = ''
        for num in problems[i]:
            if op == '+':
                solution += num
                output += f"{num} + "
            else:
                solution *= num
                output += f"{num} * "

        total += solution
        print(f"{output} = {solution} -> {total}")

    print(f"Total of all solutions = {total}")


    
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

