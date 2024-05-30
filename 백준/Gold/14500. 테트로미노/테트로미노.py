import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
field = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

diO = [0, 1, 1]
djO = [1, 0 ,1]

diI = [[0, 0, 0], [1, 2, 3]]
djI = [[1, 2, 3], [0, 0, 0]]

diL = [[1, 2, 2], [0, 0, -1], [-1, -2, -2], [0, 0, 1], [1, 2, 2], [0, 0, 1], [-1, -2, -2], [0, 0, -1]]
djL = [[0, 0, 1], [1, 2, 2], [0, 0, -1], [-1, -2, -2], [0, 0, -1], [1, 2, 2], [0, 0, 1], [-1, -2, -2]]

diZ = [[1, 1, 2], [0, -1, -1], [1, 1, 2], [0, 1, 1]]
djZ = [[0, 1, 1], [1, 1, 2], [0, -1, -1], [1, 1, 2]]

diT = [[0, 0, 1], [-1, -1, -2], [0, 0, -1], [1, 1, 2]]
djT = [[1, 2, 1], [0, 1, 0], [-1, -2, -1], [-1, 0, 0]]

ans = 0

for i in range(N):
    for j in range(M):
        tempSum = field[i][j]
        for mode in range(3):
            ni = i + diO[mode]
            nj = j + djO[mode]
            if 0 <= ni < N and 0 <= nj < M:
                tempSum += field[ni][nj]
        ans = max(ans, tempSum)

for i in range(N):
    for j in range(M):
        for I in range(len(diI)):
            tempSum = field[i][j]
            for mode in range(3):
                ni = i + diI[I][mode]
                nj = j + djI[I][mode]
                if 0 <= ni < N and 0 <= nj < M:
                    tempSum += field[ni][nj]
            ans = max(ans, tempSum)

for i in range(N):
    for j in range(M):
        for L in range(len(diL)):
            tempSum = field[i][j]
            for mode in range(3):
                ni = i + diL[L][mode]
                nj = j + djL[L][mode]
                if 0 <= ni < N and 0 <= nj < M:
                    tempSum += field[ni][nj]
            ans = max(ans, tempSum)

for i in range(N):
    for j in range(M):
        for Z in range(len(diZ)):
            tempSum = field[i][j]
            for mode in range(3):
                ni = i + diZ[Z][mode]
                nj = j + djZ[Z][mode]
                if 0 <= ni < N and 0 <= nj < M:
                    tempSum += field[ni][nj]
            ans = max(ans, tempSum)

for i in range(N):
    for j in range(M):
        for T in range(len(diT)):
            tempSum = field[i][j]
            for mode in range(3):
                ni = i + diT[T][mode]
                nj = j + djT[T][mode]
                if 0 <= ni < N and 0 <= nj < M:
                    tempSum += field[ni][nj]
            ans = max(ans, tempSum)

print(ans)