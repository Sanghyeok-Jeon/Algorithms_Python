import sys
from collections import deque

input = sys.stdin.readline

N, M, R = map(int, input().split())
g = [[]for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)

for i in range(N + 1):
    g[i].sort()

dist = [-1]* (N + 1)
dist[R] = 0
cnt = 1
answer = 0

q = deque([R])
while q:
    u = q.popleft()
    for v in g[u]:
        if dist[v] == -1:
            cnt += 1
            depth = dist[u] + 1
            dist[v] = depth
            q.append(v)
            answer += depth * cnt

print(answer)