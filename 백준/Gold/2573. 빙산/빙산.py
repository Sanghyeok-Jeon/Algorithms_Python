import sys
sys.setrecursionlimit(100000)

def DFS(i, j):
    global data
    visited[i][j] = 1

    for mode in range(4):
        ni = i + di[mode]
        nj = j + dj[mode]
        if data[ni][nj] == 0 and visited[ni][nj] == 0 and data[i][j] > 0:
            data[i][j] -= 1
        if data[ni][nj] > 0 and visited[ni][nj] == 0:
            DFS(ni, nj)

N, M = map(int, sys.stdin.readline().split())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

answer = 0
cntYear = 0
while True:
    cntIce = 0
    visited = [[0]*M for _ in range(N)]
    for i in range(1, N-1):
        for j in range(1, M-1):
            if data[i][j] > 0 and visited[i][j] == 0:
                cntIce += 1
                DFS(i, j)

    if cntIce == 0:
        break

    if cntIce >= 2:
        answer = cntYear
        break

    cntYear += 1

print(answer)