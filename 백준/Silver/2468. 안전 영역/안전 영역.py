import sys
sys.setrecursionlimit(10000)

def DFS(i, j):
    global N, rain_height

    di = [1, -1, 0, 0]
    dj = [0, 0, 1, -1]

    for mode in range(4):
        ni = i + di[mode]
        nj = j + dj[mode]
        if 0 <= ni < N and 0 <= nj < N and area[ni][nj] > rain_height and visited[ni][nj] == 0:
            visited[ni][nj] = 1
            DFS(ni, nj)

N = int(input())
area = [list(map(int, input().split())) for _ in range(N)]

rain_height = 0
safe_area = 0
while True:
    visited = [[0] * N for _ in range(N)]
    temp_safe_area = 0
    for i in range(N):
        for j in range(N):
            if area[i][j] > rain_height and visited[i][j] == 0:
                temp_safe_area += 1
                visited[i][j] = 1
                DFS(i, j)

    if temp_safe_area == 0:
        break

    if temp_safe_area > safe_area:
        safe_area = temp_safe_area

    rain_height += 1

print(safe_area)