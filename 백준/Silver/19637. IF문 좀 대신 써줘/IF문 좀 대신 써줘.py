import sys
from bisect import bisect_left

input = sys.stdin.readline

n, m = map(int, input().split())
titles = []
limits = []

for _ in range(n):
    title, limit = input().split()
    titles.append(title)
    limits.append(int(limit))

for _ in range(m):
    power = int(input())
    idx = bisect_left(limits, power)
    print(titles[idx])