#!/usr/bin/env python3

import sys
import re

num_tests = int(sys.argv[1])
print(f"num_tests: {num_tests}")

if num_tests >= 10:
    sys.exit()

assert num_tests >= 1

path = "src/vector_list/bench.cpp"

with open(path, "r", encoding="utf-8") as f:
    text = f.read()

# run N of 10 tests
text = re.sub(
    r'(sizes\s*=\s*\{' + ",".join(['[^,]+']*num_tests) + ")",
    r'\1 }; // ',
    text
)

with open(path, "w", encoding="utf-8") as f:
    f.write(text)
