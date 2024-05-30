import copy

def move(board, direction):
    n = len(board)

    if direction == 0:    # 위로 이동
        for j in range(N):
            idx = 0
            for i in range(1, N):
                if board[i][j] != 0:
                    if board[idx][j] == 0:    # 값이 없을 때
                        board[idx][j] = board[i][j]
                        board[i][j] = 0
                    elif board[idx][j] == board[i][j]:    # 값이 같을 때
                        board[idx][j] *= 2
                        board[i][j] = 0
                        idx += 1
                    else:    # 그 외 이동할 수 없는 경우
                        idx += 1
                        board[idx][j] = board[i][j]
                        if idx != i:
                            board[i][j] = 0
    elif direction == 1:    # 아래로 이동
        for j in range(N):
            idx = N - 1
            for i in range(N - 2, -1, -1):
                if board[i][j] != 0:
                    if board[idx][j] == 0:
                        board[idx][j]= board[i][j]
                        board[i][j] = 0
                    elif board[idx][j] == board[i][j]:
                        board[idx][j] *= 2
                        board[i][j] = 0
                        idx -= 1
                    else:
                        idx -= 1
                        board[idx][j] = board[i][j]
                        if idx != i:
                            board[i][j] = 0
    elif direction == 2:    # 왼쪽으로 이동
        for i in range(N):
            idx = 0
            for j in range(1, N):
                if board[i][j] != 0:
                    if board[i][idx] == 0:
                        board[i][idx] = board[i][j]
                        board[i][j] = 0
                    elif board[i][idx] == board[i][j]:
                        board[i][idx] *= 2
                        board[i][j] = 0
                        idx += 1
                    else:
                        idx += 1
                        board[i][idx] = board[i][j]
                        if idx != j:
                            board[i][j] = 0
    elif direction == 3:    # 오른쪽으로 이동
        for i in range(N):
            idx = N - 1
            for j in range(N -2, -1, -1):
                if board[i][j] != 0:
                    if board[i][idx] == 0:
                        board[i][idx] = board[i][j]
                        board[i][j] = 0
                    elif board[i][idx] == board[i][j]:
                        board[i][idx] *= 2
                        board[i][j] = 0
                        idx -= 1
                    else:
                        idx -= 1
                        board[i][idx] = board[i][j]
                        if idx != j:
                            board[i][j] = 0

    return board

def dfs(board, count):
    global answer

    # 5번 이동했으면 최댓값 갱신
    if count == 5:
        for i in range(N):
            for j in range(N):
                answer = max(answer, board[i][j])
        return

    for i in range(4):
        new_board = copy.deepcopy(board)
        new_board = move(new_board, i)
        dfs(new_board, count + 1)

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

answer = 0
dfs(board, 0)

print(answer)