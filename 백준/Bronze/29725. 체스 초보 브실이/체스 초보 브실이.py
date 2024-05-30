board = [list(input()) for _ in range(8)]

score_white = 0
score_black = 0
for i in range(8):
    for j in range(8):
        if board[i][j] == 'P':
            score_white += 1
        elif board[i][j] == 'p':
            score_black += 1
        elif board[i][j] == 'N':
            score_white += 3
        elif board[i][j] == 'n':
            score_black += 3
        elif board[i][j] == 'B':
            score_white += 3
        elif board[i][j] == 'b':
            score_black += 3
        elif board[i][j] == 'R':
            score_white += 5
        elif board[i][j] == 'r':
            score_black += 5
        elif board[i][j] == 'Q':
            score_white += 9
        elif board[i][j] == 'q':
            score_black += 9

print(score_white - score_black)