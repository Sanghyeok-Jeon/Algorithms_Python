import sys
sys.setrecursionlimit(1000000)

def DFS(i, j):
    global cnt

    for mode in range(4):
        ni = i + di[mode]
        nj = j + dj[mode]
        if 0 <= ni < n and 0 <= nj < m and data[ni][nj] == 1:
            data[ni][nj] = 0
            cnt += 1
            DFS(ni, nj)

n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

cnt_draw = 0
max_draw = 0
for i in range(n):
    for j in range(m):
        if data[i][j]:
            cnt = 1
            cnt_draw += 1
            data[i][j] = 0
            DFS(i, j)
            max_draw = max(max_draw, cnt)

print(cnt_draw)
print(max_draw)