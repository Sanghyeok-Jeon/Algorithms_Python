import sys
sys.setrecursionlimit(10**6)

def dfs(node, distance):
    global max_distance
    visited[node]= True
    max_distance = max(max_distance, distance)

    for neighbor, weight in graph[node]:
        if not visited[neighbor]:
            dfs(neighbor, distance + weight)

n = int(sys.stdin.readline().strip())
graph = [[]for _ in range(n + 1)]

for _ in range(n - 1):
    u, v, w = map(int, sys.stdin.readline().strip().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

visited = [False]* (n + 1)
max_distance = 0

dfs(1, 0)

print(max_distance)