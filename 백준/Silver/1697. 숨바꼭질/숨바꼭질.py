import sys
import collections

N, K = map(int, sys.stdin.readline().split())
q = collections.deque()
q.append((0, N))
result = 0
visited = [0] * 100001

while q:
    second, X = q.popleft()
    if X == K:
        result = second
        break
    if visited[X] == 0:
        visited[X] = 1
        if X - 1 >= 0:
            q.append((second + 1, X - 1))
        if X + 1 <= 100000:
            q.append((second + 1, X + 1))
        if 2 * X <= 100000:
            q.append((second + 1, 2 * X))

print(result)