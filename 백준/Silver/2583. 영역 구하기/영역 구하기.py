import sys
sys.setrecursionlimit(10000)

def DFS(i, j):
    global temp_cnt

    field[i][j] = 1
    di = [1, -1, 0, 0]
    dj = [0, 0, 1, -1]

    for mode in range(4):
        ni = i + di[mode]
        nj = j + dj[mode]
        if 0 <= ni < M and 0 <= nj < N and field[ni][nj] == 0:
            field[ni][nj] = 1
            temp_cnt += 1
            DFS(ni, nj)

M, N, K = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(K)]
field = [[0]*N for _ in range(M)]

for i in range(len(data)):
    for j in range(data[i][1], data[i][3]):
        for k in range(data[i][0], data[i][2]):
            field[j][k] = 1

cnt_fields = []

for i in range(M):
    for j in range(N):
        if field[i][j] == 0:
            temp_cnt = 1
            field[i][j] = 1
            DFS(i, j)
            cnt_fields.append(temp_cnt)

cnt_fields.sort()
print(len(cnt_fields))
for i in range(len(cnt_fields)):
    print(cnt_fields[i], end=' ')
print()