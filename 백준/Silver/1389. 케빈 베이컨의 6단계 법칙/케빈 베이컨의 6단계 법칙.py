import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
graph = [[N]*(N+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, N+1):
        if i == j:
            graph[i][j] = 0

for _ in range(M):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    graph[x][y] = 1
    graph[y][x] = 1

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

ans = [0] * (N+1)
for i in range(1, N+1):
    for j in range(1, N+1):
        if i != j:
            ans[i] += graph[i][j]

print(ans.index(min(ans[1:])))