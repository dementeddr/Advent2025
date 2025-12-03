#!/usr/bin/python3
import re

pat = re.compile(r"(\d+)\1+")

arr = {123123, 121212, 111}

for num in arr:
    res = pat.match(str(num))

    print(f"{num}: {res.group(1)}")
        
