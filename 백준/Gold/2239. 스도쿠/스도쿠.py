def is_valid(board, row, col, num):
    # 행에 중복된 숫자가 있는지 확인
    if num in board[row]:
        return False

    # 열에 중복된 숫자가 있는지 확인
    for i in range(9):
        if board[i][col] == num:
            return False

    # 3x3 박스에 중복된 숫자가 있는지 확인
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:    # 빈 칸인 경우
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num

                        if solve_sudoku(board):    # 다음 빈 칸을 채우기 위해 호출
                            return True

                        board[row][col] = 0    # 해결할 수 없는 경우, 다시 빈 칸으로 되돌림

                return False    # 1부터 9까지의 숫자를 모두 시도해도 해결할 수 없는 경우

    return True    # 모든 빈 칸을 채웠을 때



board = [list(map(int, input())) for _ in range(9)]

solve_sudoku(board)

for row in board:
    print(''.join(map(str, row)))