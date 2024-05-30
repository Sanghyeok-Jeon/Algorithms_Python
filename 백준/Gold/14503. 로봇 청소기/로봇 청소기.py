N, M = map(int, input().split())
r, c, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

count = 1
board[r][c] = 2    # 청소한 위치는 2로 표시

while True:
    clean = False
    for _ in range(4):
        d = (d + 3) % 4
        nx = r + dx[d]
        ny = c + dy[d]
        if board[nx][ny] == 0:    # 청소되지 않은 빈 칸이 있는 경우
            count += 1
            r, c = nx, ny
            board[r][c] = 2
            clean = True
            break

    # 청소되지 않은 빈 칸이 없는 경우
    if not clean:
        if board[r - dx[d]][c - dy[d]] == 1:    # 후진할 수 없으면 작동을 멈춤
            break
        else:    # 바라보는 방향을 유지한 채로 한 칸 후진
            r = r - dx[d]
            c = c - dy[d]

print(count)