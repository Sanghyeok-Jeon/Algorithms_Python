def check_bingo():
    bingo = 0

    for i in range(5):
        if sum(selected_board[i]) == 5:
            bingo += 1

    for j in range(5):
        tmp_cnt = 0
        for i in range(5):
            if selected_board[i][j]:
                tmp_cnt += 1

        if tmp_cnt == 5:
            bingo += 1

    tmp_cnt = 0
    for i in range(5):
        if selected_board[i][i]:
            tmp_cnt += 1
    if tmp_cnt == 5:
        bingo += 1

    tmp_cnt = 0
    for i in range(5):
        if selected_board[i][-(i + 1)]:
            tmp_cnt += 1
    if tmp_cnt == 5:
        bingo += 1

    return bingo

def board_select(cnt):
    for i in range(5):
        for j in range(5):
            cnt += 1
            for k in range(5):
                for l in range(5):
                    if board[k][l] == order[i][j]:
                        selected_board[k][l] = True

            bingo = check_bingo()

            if bingo >= 3:
                return cnt
    return cnt

board = [list(map(int, input().split())) for _ in range(5)]
order = [list(map(int, input().split())) for _ in range(5)]

selected_board = [[False] * 5 for _ in range(5)]
cnt = board_select(0)

print(cnt)