M, N = map(int, input().split())

road = [[0] * N for _ in range(M)]
move = 0
i, j = 0, 0
turn = 0

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
mode = 0
road[i][j] = 1

while True:
    move += 1

    if move == M * N:
        print(turn)
        break

    nx = i + dx[mode]
    ny = j + dy[mode]
    if 0 <= nx < M and 0 <= ny < N and road[nx][ny] == 0:
        road[i][j] = 1
        i, j = nx, ny
    else:
        road[i][j] = 1
        turn += 1
        mode = (mode + 1) % 4
        i += dx[mode]
        j += dy[mode]