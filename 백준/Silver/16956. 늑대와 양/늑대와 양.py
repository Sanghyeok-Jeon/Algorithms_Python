R, C = map(int, input().split())
farm = [input() for _ in range(R)]

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

possible = True
for i in range(R):
    for j in range(C):
        if farm[i][j] == 'S':
            for mode in range(4):
                ni = i + di[mode]
                nj = j + dj[mode]
                if 0 <= ni < R and 0 <= nj < C:
                    if farm[ni][nj] == 'W':
                        possible = False
                        break
        if not possible:
            break
    if not possible:
        break

if not possible:
    print(0)
else:
    print(1)
    for i in range(R):
        print(farm[i].replace('.', 'D'))