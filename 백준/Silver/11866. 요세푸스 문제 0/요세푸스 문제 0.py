import sys
import collections

N, K = map(int, sys.stdin.readline().split())
q = collections.deque(range(1, N+1))

print('<', end='')
while len(q) > 1:
    for _ in range(K-1):
        q.append(q.popleft())
    print(q.popleft(), end=', ')
print(q.popleft(), end='')
print('>')