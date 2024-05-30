import sys
def backtracking(i, j, tmp):
    if len(tmp) == 6:
        numbers.add(tmp)
        return

    di = [1, -1, 0, 0]
    dj = [0, 0, 1, -1]
    for mode in range(4):
        ni = i + di[mode]
        nj = j + dj[mode]
        if 0 <= ni < 5 and 0 <= nj < 5:
            backtracking(ni, nj, tmp+data[ni][nj])

data = [list(sys.stdin.readline().split()) for _ in range(5)]
numbers = set()

for i in range(5):
    for j in range(5):
        backtracking(i, j, data[i][j])

print(len(numbers))