import sys
sys.setrecursionlimit(10**6)

def dfs(graph, visited, order, node, counter):
    visited[node] = True
    order[node] = counter[0]
    counter[0] += 1

    for neighbor in sorted(graph[node]):
        if not visited[neighbor]:
            dfs(graph, visited, order, neighbor, counter)

import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = {i: [] for i in range(1, n + 1)}

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (n + 1)
order = [0] * (n + 1)
counter = [1]

dfs(graph, visited, order, r, counter)

for i in range(1, n + 1):
    print(order[i])