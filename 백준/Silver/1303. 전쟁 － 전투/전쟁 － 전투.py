def DFSB(i, j):
    global cnt
    visited[i][j] = 1
    cnt += 1

    for mode in range(4):
        ni = i + di[mode]
        nj = j + dj[mode]
        if 0 <= ni < M and 0 <= nj < N and visited[ni][nj] == 0 and field[ni][nj] == 'B':
            DFSB(ni, nj)

def DFSW(i, j):
    global cnt
    visited[i][j] = 1
    cnt += 1

    for mode in range(4):
        ni = i + di[mode]
        nj = j + dj[mode]
        if 0 <= ni < M and 0 <= nj < N and visited[ni][nj] == 0 and field[ni][nj] == 'W':
            DFSW(ni, nj)

N, M = map(int, input().split())
field = [list(input()) for _ in range(M)]
visited = [[0]*N for _ in range(M)]
our = 0
enemy = 0

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

for i in range(M):
    for j in range(N):
        if field[i][j] == 'B' and visited[i][j] == 0:
            cnt = 0
            DFSB(i, j)
            enemy += cnt**2
        if field[i][j] == 'W' and visited[i][j] == 0:
            cnt = 0
            DFSW(i, j)
            our += cnt**2

print('{} {}'.format(our, enemy))