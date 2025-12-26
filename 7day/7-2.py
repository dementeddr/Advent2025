#!/usr/bin/python3

import sys
import re
from time import perf_counter_ns

_day = 7 #Advent of Code day

## BEGIN SOLUTION

def main(data):

    beams = [0 for _ in range(len(data[0]))]
    start = data[0].find("S")
    beams[start] = 1
    count = 0

    for line in data[1:]:
        new_beams = beams.copy()
        
        for i, x in enumerate(line):
            if x == '^' and new_beams[i] > 0:
                splits = new_beams[i]
                new_beams[i] = 0
                new_beams[i-1] += splits
                new_beams[i+1] += splits 

                print(f"{splits} beams at x={i}. [{i-1}]={new_beams[i-1]}, [{i+1}]={new_beams[i+1]}")

        beams = new_beams
        #print(beams)
        print()

    for b in beams:
        count += b

    print(beams)
    print(f"Total beams split = {count}")



    
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

