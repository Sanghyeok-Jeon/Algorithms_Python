import sys
from collections import deque

input = sys.stdin.readline
n, m, r = map(int, input().split())

adj = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

for i in range(1, n + 1):
    adj[i].sort()

order = [0] * (n + 1)
q = deque([r])
order[r] = 1
cnt = 1

while q:
    x = q.popleft()
    for nx in adj[x]:
        if order[nx]== 0:
            cnt += 1
            order[nx]= cnt
            q.append(nx)

out = "\n".join(str(order[i]) for i in range(1, n + 1))
sys.stdout.write(out)