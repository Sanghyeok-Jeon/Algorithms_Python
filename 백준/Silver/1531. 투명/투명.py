painting = [[0] * 101 for _ in range(101)]

N, M = map(int, input().split())
for _ in range(N):
    x_left, y_left, x_right, y_right = map(int, input().split())
    for y in range(y_left, y_right + 1):
        for x in range(x_left, x_right + 1):
            painting[y][x] += 1

cnt_block = 0
for i in range(1, 101):
    for j in range(1, 101):
        if painting[i][j] > M:
            cnt_block += 1

print(cnt_block)