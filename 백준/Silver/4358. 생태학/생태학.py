import sys
from collections import defaultdict

trees = defaultdict(int)
total = 0

for line in sys.stdin:
    name = line.strip()
    if name:
        trees[name] += 1
        total += 1

for name in sorted(trees):
    percent = (trees[name] / total) * 100
    print(f"{name} {percent:.4f}")