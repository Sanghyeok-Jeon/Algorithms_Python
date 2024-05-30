import sys
sys.setrecursionlimit(1000000)

def DFS(i, j):
    visited[i][j] = 1

    for mode in range(8):
        ni = i + di[mode]
        nj = j + dj[mode]
        if 0 <= ni < M and 0 <= nj < N and banner[ni][nj] and not visited[ni][nj]:
            DFS(ni, nj)

    return

M, N = map(int, input().split())
banner = [list(map(int, input().split())) for _ in range(M)]
visited = [[0]*N for _ in range(M)]

di = [-1, -1, 0, 1, 1, 1, 0, -1]
dj = [0, 1, 1, 1, 0, -1, -1, -1]

cnt = 0
for i in range(M):
    for j in range(N):
        if banner[i][j] and not visited[i][j]:
            cnt += 1
            DFS(i, j)

print(cnt)