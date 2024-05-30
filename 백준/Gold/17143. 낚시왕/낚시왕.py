import sys
input = sys.stdin.readline

def catch_shark(j, board):
    weight_shark = 0
    for i in range(1, R + 1):
        if board[i][j]:
            weight_shark = board[i][j][0][2]
            board[i][j] = []
            break

    return weight_shark, board

def move_shark(board):
    tmpBoard = [[[] for _ in range(C + 1)] for _ in range(R + 1)]

    for i in range(1, R + 1):
        for j in range(1, C + 1):
            if board[i][j]:
                x, y = i, j
                s, d, z = board[i][j][0]
                distance = s

                while distance:
                    x = x + dx[d]
                    y = y + dy[d]
                    if 1 <= x < (R + 1) and 1 <= y < (C + 1):
                        distance -= 1
                    else:    # 경계를 넘는 순간 방향 전환
                        x = x - dx[d]
                        y = y - dy[d]
                        
                        if d == 1:
                            d = 2
                        elif d == 2:
                            d = 1
                        elif d == 3:
                            d = 4
                        else:
                            d = 3

                if len(tmpBoard[x][y]) == 1:    # 같은 자리에 다른 상어가 있는 경우 크기 비교
                    if tmpBoard[x][y][0][2] < z:
                        tmpBoard[x][y] = [[s, d, z]]
                else:
                    tmpBoard[x][y].append([s, d, z])

    return tmpBoard

R, C, M = map(int, input().split())
board = [[[] for _ in range(C + 1)] for _ in range(R + 1)]
for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    board[r][c].append([s, d, z])    # 속력, 이동방향, 크기

# 상하우좌 방향
dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, 1, -1]

result = 0
for j in range(1, C + 1):
    weight_shark, board = catch_shark(j, board)
    result += weight_shark
    board = move_shark(board)

print(result)