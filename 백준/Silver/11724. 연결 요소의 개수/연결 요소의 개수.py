import sys
sys.setrecursionlimit(10000)

def DFS(i):
    visited[i] = 1
    for j in range(1, N+1):
        if graph[i][j] and visited[j] == 0:
            DFS(j)

    return

N, M = map(int, sys.stdin.readline().split())
graph = [[0]*(N+1) for _ in range(N+1)]
for i in range(M):
    x, y = map(int, sys.stdin.readline().split())
    graph[x][y] = 1
    graph[y][x] = 1
visited = [0] * (N+1)

connect = 0
for i in range(1, N+1):
    if visited[i] == 0:
        connect += 1
        DFS(i)

print(connect)