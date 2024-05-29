import sys
sys.setrecursionlimit(50000)

def DFS(i, j):
    field[i][j] = 0

    di = [1, -1, 0, 0]
    dj = [0, 0, 1, -1]

    for mode in range(4):
        ni = i + di[mode]
        nj = j + dj[mode]
        if 0 <= ni < N and 0 <= nj < M and field[ni][nj]:
            DFS(ni, nj)

T = int(input())

for tc in range(T):
    N, M, K = map(int, input().split())
    field = [[0]*M for _ in range(N)]
    for _ in range(K):
        i, j = map(int, input().split())
        field[i][j] = 1

    worms = 0
    for i in range(N):
        for j in range(M):
            if field[i][j]:
                DFS(i, j)
                worms += 1

    print(worms)