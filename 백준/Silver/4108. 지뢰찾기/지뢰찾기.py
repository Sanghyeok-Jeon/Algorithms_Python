dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1 ,-1, -1]

while True:
    R, C = map(int, input().split())

    if R == 0 and C == 0:
        break

    field = [list(input()) for _ in range(R)]

    answer = [[''] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if field[i][j] == '*':
                answer[i][j] = '*'
            else:
                cnt = 0
                for mode in range(8):
                    nx = i + dx[mode]
                    ny = j + dy[mode]
                    if 0 <= nx < R and 0 <= ny < C and field[nx][ny] == '*':
                        cnt += 1

                answer[i][j] = str(cnt)

    for i in range(R):
        print(''.join(answer[i]))