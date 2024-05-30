import sys

import itertools
for data in itertools.combinations(map(int, sys.stdin.readlines()), 7):
    if sum(data) == 100:
        print(*sorted(data), sep='\n')