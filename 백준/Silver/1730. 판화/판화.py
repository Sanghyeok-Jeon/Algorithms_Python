def cutting(d, i, j):
    if board[i][j] == chr(46): # '.'
        if d == 'U' or d == 'D':
            board[i][j] = chr(124)
        else:
            board[i][j] = chr(45)
    elif board[i][j] == chr(124): # '|'
        if d == 'L' or d == 'R':
            board[i][j] = chr(43) # '+'
    elif board[i][j] == chr(45): # '-'
        if d == 'U' or d == 'D':
            board[i][j] = chr(43) # '+'

    return

N = int(input())
direction = input()

board = [['.'] * N for _ in range(N)]

i, j = 0, 0
for d in direction:
    ni, nj = i, j
    if d == 'U':
        ni -= 1
    elif d == 'D':
        ni += 1
    elif d == 'L':
        nj -= 1
    elif d == 'R':
        nj += 1

    if 0 <= ni < N and 0 <= nj < N:
        cutting(d, i, j)
        i, j = ni, nj
        cutting(d, i, j)

for i in range(N):
    print(''.join(board[i]))