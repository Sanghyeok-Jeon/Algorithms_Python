from collections import defaultdict
import sys
sys.setrecursionlimit(2000)
input = sys.stdin.readline

def dfs(node, depth):
    if depth == 4:
        return True

    visited[node] = True

    for neighbor in graph[node]:
        if not visited[neighbor]:
            if dfs(neighbor, depth + 1):
                return True

    visited[node] = False

    return False

N, M = map(int, input().split())

graph = defaultdict(list)
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * N

for i in range(N):
    if dfs(i, 0):
        exit(print(1))

print(0)

