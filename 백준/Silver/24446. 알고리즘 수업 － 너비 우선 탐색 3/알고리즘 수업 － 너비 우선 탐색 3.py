import sys
from collections import deque

input = sys.stdin.readline

N, M, R = map(int, input().split())
g = [[]for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)

dist = [-1]* (N + 1)
dist[R] = 0

q = deque([R])
while q:
    u = q.popleft()
    for v in g[u]:
        if dist[v] == -1:
            dist[v] = dist[u] + 1
            q.append(v)

print("\n".join(str(dist[i]) for i in range(1, N + 1)))