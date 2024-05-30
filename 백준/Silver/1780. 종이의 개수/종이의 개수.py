import sys

def checkPaper(i, j, l):
    global paperZero, paperOne, paperMinusOne

    if l == 0:
        return

    needDivide = False
    target = paper[i][j]
    for x in range(i, i+l):
        for y in range(j, j+l):
            if target != paper[x][y]:
                needDivide = True
                break
    if needDivide:
        l //= 3
        checkPaper(i, j, l)
        checkPaper(i, j + l, l)
        checkPaper(i, j + l * 2, l)
        checkPaper(i + l, j, l)
        checkPaper(i + l, j + l, l)
        checkPaper(i + l, j + l * 2, l)
        checkPaper(i + l * 2, j, l)
        checkPaper(i + l * 2, j + l, l)
        checkPaper(i + l * 2, j + l * 2, l)
    else:
        if target == 0:
            paperZero += 1
            return
        elif target == 1:
            paperOne += 1
            return
        elif target == -1:
            paperMinusOne += 1
            return


N = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
paperZero, paperOne, paperMinusOne = 0, 0, 0

checkPaper(0, 0, N)

print(paperMinusOne)
print(paperZero)
print(paperOne)