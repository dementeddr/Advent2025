#!/usr/bin/python3

import sys
import re
from time import perf_counter_ns

_day = 4 #Advent of Code day

## BEGIN SOLUTION

def main(data):

    grid = list(map(list, data))
    total = 0

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == '@' and count_adj(grid, x, y) < 4:
                grid[y][x] = 'x'
                total += 1

    list(map(lambda l: print(''.join(l)), grid))
    print(f"\nFree rolls: {total}")


def count_adj(grid, x, y):
    count = 0
    for dy in range(-1,2): 
        for dx in range(-1, 2):
            if dx == 0 and dy == 0:
                continue
            if is_in_grid(grid, x+dx, y+dy) and grid[y+dy][x+dx] != '.':
                count += 1
    return count


def is_in_grid(grid, x, y):
    return 0 <= y < len(grid) and 0 <= x < len(grid[y])

    
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

