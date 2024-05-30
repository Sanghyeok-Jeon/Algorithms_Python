N = int(input())
room = [input()+'X' for _ in range(N)] + ['X' * (N+1)]

possibleX, possibleY = 0, 0
for i in range(N+1):
    cntX, cntY = 0, 0
    for j in range(N+1):
        if room[i][j] == '.':
            cntX += 1
        else:
            if cntX >= 2:
                possibleX += 1
            cntX = 0

        if room[j][i] == '.':
            cntY += 1
        else:
            if cntY >= 2:
                possibleY += 1
            cntY = 0

print(possibleX, possibleY)