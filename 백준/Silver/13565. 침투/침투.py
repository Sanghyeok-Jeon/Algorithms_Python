import sys
sys.setrecursionlimit(1000000)

def DFS(i, j):
    global current
    if i == M-1:
        current = 1
        return

    visited[i][j] = 1

    for mode in range(4):
        ni = i + di[mode]
        nj = j + dj[mode]
        if 0 <= ni < M and 0 <= nj < N:
            if fiber[ni][nj] == '0' and visited[ni][nj] == 0:
                DFS(ni, nj)  
                
M, N = map(int, sys.stdin.readline().split())
fiber = [list(sys.stdin.readline()) for _ in range(M)]
visited = [[0]*N for _ in range(M)]

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

current = 0
for j in range(N):
    if current == 0:
        if fiber[0][j] == '0' and visited[0][j] == 0:
            DFS(0, j)

print('YES' if current else 'NO')