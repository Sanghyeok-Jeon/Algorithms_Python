N, M = map(int, input().split())
castle = [input() for _ in range(N)]

row = [0] * N
column = [0] * M

for i in range(N):
    for j in range(M):
        if castle[i][j] == 'X':
            row[i] = 1
            column[j] = 1

cntRow = row.count(0)
cntColumn = column.count(0)

print(max(cntRow, cntColumn))