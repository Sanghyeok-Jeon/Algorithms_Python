import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, n + 1):
    graph[i].sort()

visited = [0] * (n + 1)   
depth = [-1] * (n + 1)    
cnt = 1

def dfs(v: int, d: int):
    global cnt
    visited[v] = cnt
    depth[v] = d
    cnt += 1
    for nxt in graph[v]:
        if visited[nxt] == 0:
            dfs(nxt, d + 1)

dfs(r, 0)

ans = 0
for i in range(1, n + 1):
    ans += visited[i] * depth[i]

print(ans)