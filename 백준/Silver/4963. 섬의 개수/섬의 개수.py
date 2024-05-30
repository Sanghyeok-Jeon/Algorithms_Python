import sys
sys.setrecursionlimit(100000)

def DFS(i, j):
    global w, h
    for mode in range(8):
        ni = i + di[mode]
        nj = j + dj[mode]
        if 0 <= ni < h and 0 <= nj < w and land[ni][nj]:
            land[ni][nj] = 0
            DFS(ni, nj)

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    land = [list(map(int, input().split())) for _ in range(h)]
    island = 0

    di = [-1, -1, 0, 1, 1, 1, 0, -1]
    dj = [0, 1, 1, 1, 0, -1, -1, -1]

    for i in range(h):
        for j in range(w):
            if land[i][j]:
                DFS(i, j)
                island += 1

    print(island)