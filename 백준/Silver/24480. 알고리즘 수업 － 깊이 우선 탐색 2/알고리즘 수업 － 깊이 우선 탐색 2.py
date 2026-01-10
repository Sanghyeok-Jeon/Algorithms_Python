import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(node):
    global cnt
    visited[node] = True
    order[node] = cnt
    cnt += 1
    for nxt in graph[node]:
        if not visited[nxt]:
            dfs(nxt)

N, M, R = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, N + 1):
    graph[i].sort(reverse=True)

visited = [False] * (N + 1)
order = [0] * (N + 1)
cnt = 1

dfs(R)

for i in range(1, N + 1):
    print(order[i])