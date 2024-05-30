import sys

def check_possible_num(x, y, num):
    rect_x = (x // 3) * 3
    rect_y = (y // 3) * 3
    for i in range(9):
        if num == sudokuBoard[x][i]:
            return False
        if num == sudokuBoard[i][y]:
            return False
        if num == sudokuBoard[rect_x + (i // 3)][rect_y + (i % 3)]:
            return False

    return True
def sudoku(num):
    if num == len(blankCoordinate):
        for sudoLine in sudokuBoard:
            print(*sudoLine)
        exit(0)

    blank_x, blank_y = blankCoordinate[num]
    for i in range(1, 10):
        if check_possible_num(blank_x, blank_y, i):
            sudokuBoard[blank_x][blank_y] = i
            sudoku(num + 1)
            sudokuBoard[blank_x][blank_y] = 0

sudokuBoard = []
blankCoordinate = []

for i in range(9):
    sudokuBoard.append(list(map(int, sys.stdin.readline().split())))
    for j in range(9):
        if sudokuBoard[i][j] == 0:
            blankCoordinate.append((i, j))

sudoku(0)