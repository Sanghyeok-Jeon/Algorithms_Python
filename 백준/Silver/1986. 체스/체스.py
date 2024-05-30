import sys

def king(i, j):
    ki = [-1, -2, -2, -1, 1, 2, 2, 1]
    kj = [-2, -1, 1, 2, 2, 1, -1, -2]
    for mode in range(8):
        ni = i + ki[mode]
        nj = j + kj[mode]
        if 0 <= ni < n and 0 <= nj < m and chess[ni][nj] != 'K' and chess[ni][nj] != 'Q' and chess[ni][nj] != 'P':
            chess[ni][nj] = 1

def queen(i, j):
    qi = [-1, -1, 0, 1, 1, 1, 0, -1]
    qj = [0, 1, 1, 1, 0, -1, -1, -1]
    for mode in range(8):
        now_i, now_j = i, j
        while True:
            ni = now_i + qi[mode]
            nj = now_j + qj[mode]
            if 0 <= ni < n and 0 <= nj < m and chess[ni][nj] != 'K' and chess[ni][nj] != 'Q' and chess[ni][nj] != 'P':
                chess[ni][nj] = 1
                now_i = ni
                now_j = nj
            else:
                break


n, m = map(int, sys.stdin.readline().split())
chess = [[0]*m for _ in range(n)]
q = list(map(int, input().split()))
for i in range(1, len(q), 2):
    chess[q[i]-1][q[i+1]-1] = 'Q'
k = list(map(int, input().split()))
for i in range(1, len(k), 2):
    chess[k[i]-1][k[i+1]-1] = 'K'
p = list(map(int, input().split()))
for i in range(1, len(p), 2):
    chess[p[i]-1][p[i+1]-1] = 'P'

for i in range(n):
    for j in range(m):
        if chess[i][j] == 'K':
            king(i, j)
        if chess[i][j] == 'Q':
            queen(i, j)

cnt = 0
for i in range(n):
    for j in range(m):
        if chess[i][j] == 0:
            cnt += 1

print(cnt)