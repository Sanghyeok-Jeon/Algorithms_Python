import sys

from collections import deque

dq = deque()

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

for i in range(N):
    if A[i] == 0:
        dq.append(B[i])

M = int(sys.stdin.readline())
C = list(map(int, sys.stdin.readline().split()))

for i in range(M):
    dq.appendleft(C[i])
    print(dq.pop(), end=' ')