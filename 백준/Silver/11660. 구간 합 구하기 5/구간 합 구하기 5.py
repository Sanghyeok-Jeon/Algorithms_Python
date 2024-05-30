import sys

N, M = map(int, sys.stdin.readline().split())
data = [[0] * (N+1)] + [[0] + list(map(int, sys.stdin.readline().split())) for _ in range(N)]
section = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

for x in range(1, N+1):
    for y in range(1, N+1):
        data[x][y] += data[x][y-1] + data[x-1][y] - data[x-1][y-1]

for i in range(M):
    start_i, start_j, end_i, end_j = section[i][0], section[i][1], section[i][2], section[i][3]
    print(data[end_i][end_j] - data[start_i-1][end_j] - data[end_i][start_j-1] + data[start_i-1][start_j-1])