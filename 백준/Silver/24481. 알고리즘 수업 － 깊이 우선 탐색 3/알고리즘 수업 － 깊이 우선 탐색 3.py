import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def dfs(u, d):
    depth[u] = d
    for v in adj[u]:
        if depth[v] == -1:
            dfs(v, d + 1)

n, m, r = map(int, input().split())

adj = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

for i in range(1, n + 1):
    adj[i].sort()

depth = [-1] * (n + 1)

dfs(r, 0)

print("\n".join(str(depth[i]) for i in range(1, n + 1)))