import sys

A, B, C = map(int, sys.stdin.readline().rstrip().split())
if B >= C:
    print(-1)
else:
    print(A // (C - B) + 1)