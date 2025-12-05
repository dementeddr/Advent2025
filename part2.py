#!/usr/bin/python3

import os
import re

day = 0
sol_pat = re.compile(r"(\d{1,2}-)1.py")
files = []

for (dirpath, dirnames, filenames) in os.walk("."):
    files.extend(filenames)
    break

print(files)

part1_name = next((x for x in map(sol_pat.fullmatch, files) if x is not None), None)

if part1_name is None:
    print("No file matching the `dd-1.py` pattern found")
    exit(1)

print(part1_name)

file_contents = ''

with open(part1_name.group(0), "r") as p1_fp:
    file_contents = p1_fp.read()

part2_name = part1_name.groups(1) + "-2.py"

with open(part2_name, "w") as p2_fp:
    p2_fp.write(file_contents)

os.chmod(part2_name, 0o777)
