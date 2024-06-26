import sys
input = sys.stdin.readline

def is_valid_move(board, x, y, dx, dy):
    n = len(board)
    nx, ny = x + 2 * dx, y + 2 * dy
    if 0 <= nx < n and 0 <= ny < n:
        if board[x + dx][y + dy] == 2 and board[nx][ny] == 0:
            return True
    return False

def make_move(board, x, y, dx, dy):
    board[x][y] = 0
    board[x + dx][y + dy] = 0
    board[x + 2 * dx][y + 2 * dy] = 2

def undo_move(board, x, y, dx, dy):
    board[x][y] = 2
    board[x + dx][y + dy] = 2
    board[x + 2 * dx][y + 2 * dy] = 0

def count_stones(board):
    return sum(row.count(2) for row in board)

def can_win(board):
    if count_stones(board) == 1:
        return True

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

    for x in range(N):
        for y in range(N):
            if board[x][y] == 2:
                for dx, dy in directions:
                    if is_valid_move(board, x, y, dx, dy):
                        make_move(board, x, y, dx, dy)
                        if can_win(board):
                            return True
                        undo_move(board, x, y, dx, dy)

    return False

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

if can_win(board):
    print("Possible")
else:
    print("Impossible")