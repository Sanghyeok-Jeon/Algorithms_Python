import sys

def checkColor(i, j, l):
    target = paper[i][j]
    for x in range(i, i+l):
        for y in range(j, j+l):
            if paper[x][y] != target:
                return False
    return True

def makeColoredPaper(i, j, l):
    global white, blue

    if checkColor(i, j, l):
        if paper[i][j]:
            blue += 1
        else:
            white += 1
    else:
        l //= 2
        makeColoredPaper(i, j, l)
        makeColoredPaper(i+l, j, l)
        makeColoredPaper(i, j+l, l)
        makeColoredPaper(i+l, j+l, l)
    return

N = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
white, blue = 0, 0

makeColoredPaper(0, 0, N)

print(white)
print(blue)