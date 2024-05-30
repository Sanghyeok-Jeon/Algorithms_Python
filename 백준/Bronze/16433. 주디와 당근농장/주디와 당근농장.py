import sys
sys.setrecursionlimit(10000000)

def Carrot(i, j):
    farm[i][j] = 'v'

    for mode in range(4):
        ni = i + di[mode]
        nj = j + dj[mode]
        if 0 <= ni < N and 0 <= nj < N and farm[ni][nj] == '.':
            Carrot(ni, nj)

N, R, C = map(int, input().split())
farm = [['.']*N for _ in range(N)]
r, c = R-1, C-1

di = [-1, -1, 1, 1]
dj = [-1, 1, 1, -1]
Carrot(r, c)

for i in range(N):
    print(''.join(farm[i]))