n = int(input())
mine = [input() for _ in range(n)]
board = [list(input()) for _ in range(n)]

di = [-1, -1, 0, 1, 1, 1, 0, -1]
dj = [0, 1, 1, 1, 0, -1, -1, -1]

mine_boom = False
for i in range(n):
    for j in range(n):
        if board[i][j] == 'x':
            if mine[i][j] == '*':
                mine_boom = True

            cnt_mine = 0
            for mode in range(8):
                ni = i + di[mode]
                nj = j + dj[mode]
                if 0 <= ni < n and 0 <= nj < n and mine[ni][nj] == '*':
                    cnt_mine += 1

            board[i][j] = str(cnt_mine)

if mine_boom:
    for i in range(n):
        for j in range(n):
            if mine[i][j] == '*':
                board[i][j] = '*'

for i in range(n):
    print(''.join(board[i]))