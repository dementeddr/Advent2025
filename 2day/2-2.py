#!/usr/bin/python3

import sys
import re
from time import perf_counter_ns

_day = 2 #Advent of Code day

## BEGIN SOLUTION

def main(data):

    id_pat = re.compile(r"(\d+)\1+")
    ranges = data[0].split(",")
    count = 0

    for rang in ranges:
        ends = list(map(int, rang.split("-")))
        print(rang)

        for i in range(ends[0], ends[1]+1):
            text = str(i)

            if id_pat.fullmatch(text):
                count += i
                print(f"  {text}")

    print(f"Total: {count}")


    
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

