import sys
from itertools import permutations

input = sys.stdin.readline

n = int(input().strip())
arr = list(map(int, input().split()))

ans = 0

for perm in permutations(arr, n):
    s = 0
    for i in range(n - 1):
        s += abs(perm[i] - perm[i + 1])
    if s > ans:
        ans = s

print(ans)