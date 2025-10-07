N = int(input())
target = int(input())

board = [[0] * N for _ in range(N)]
target_i = 0
target_j = 0

num = 1
i = N // 2
j = N // 2

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
mode = 0

len_num = 1
len_cnt = 0
len_now = 0

board[i][j] = num
if num == target:
    target_i = i + 1
    target_j = j + 1

while num < N ** 2:
    len_now += 1
    i = i + di[mode]
    j = j + dj[mode]

    num += 1
    board[i][j] = num

    if num == target:
        target_i = i + 1
        target_j = j + 1

    if len_now == len_num:
        mode = (mode + 1) % 4
        len_now = 0
        len_cnt += 1

    if len_cnt == 2:
        len_cnt = 0
        len_num += 1

for idx in range(N):
    print(*board[idx])
print(target_i, target_j)