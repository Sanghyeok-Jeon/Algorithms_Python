import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline

s = input().strip()
q = int(input())

pos = [[] for _ in range(26)]

for i, ch in enumerate(s):
    pos[ord(ch) - ord('a')].append(i)

for _ in range(q):
    a, l, r = input().split()
    l = int(l)
    r = int(r)

    arr = pos[ord(a) - ord('a')]
    print(bisect_right(arr, r) - bisect_left(arr, l))