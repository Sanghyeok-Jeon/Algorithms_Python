import sys
sys.setrecursionlimit(100000)

def DFS(i, j):
    visited[i][j] = 1

    for mode in range(4):
        ni = i + di[mode]
        nj = j + dj[mode]
        if 0 <= ni < H and 0 <= nj < W:
            if grid[ni][nj] == '#' and visited[ni][nj] == 0:
                DFS(ni, nj)

T = int(input())

for tc in range(T):
    H, W = map(int, input().split())
    grid = [input() for _ in range(H)]
    visited = [[0]*W for _ in range(H)]

    di = [1, -1, 0, 0]
    dj = [0, 0, 1, -1]

    sheep = 0
    for i in range(H):
        for j in range(W):
            if not visited[i][j]:
                if grid[i][j] == '#':
                    sheep += 1
                    DFS(i, j)

    print(sheep)