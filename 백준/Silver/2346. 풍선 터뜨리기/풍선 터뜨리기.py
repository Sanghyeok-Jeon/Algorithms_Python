import sys
from collections import deque

N = int(input())
dq = deque(enumerate(map(int, sys.stdin.readline().split())))

while dq:
    idx, boom = dq.popleft()
    print(idx + 1, end=' ')
    dq.rotate(-(boom-1)) if boom > 0 else dq.rotate(-boom)