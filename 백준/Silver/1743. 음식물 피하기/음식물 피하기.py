import sys
sys.setrecursionlimit(10000)

def DFS(i, j):
    global cnt

    for mode in range(4):
        ni = i + di[mode]
        nj = j + dj[mode]
        if 0 <= ni < N+1 and 0 <= nj < M+1 and uumth[ni][nj] == 1:
            cnt += 1
            uumth[ni][nj] = 0
            DFS(ni, nj)

N, M, K = map(int, input().split())
uumth = [[0]*(M+1) for _ in range(N+1)]
for _ in range(K):
    r, c = map(int, input().split())
    uumth[r][c] = 1

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

max_cnt = 0
for i in range(1, N+1):
    for j in range(1, M+1):
        if uumth[i][j]:
            cnt = 1
            uumth[i][j] = 0
            DFS(i, j)
            max_cnt = max(max_cnt, cnt)

print(max_cnt)