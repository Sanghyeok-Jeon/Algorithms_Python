import sys

def checkQuadTree(n, y, x):
    if n == 1:
        print(video[y][x], end="")
        return

    checkSame = True
    for i in range(y, y+n):
        for j in range(x, x+n):
            if video[i][j] != video[y][x]:
                checkSame = False
                break
        if not checkSame:
            break

    if checkSame:
        print(video[y][x], end="")
    else:
        n //= 2
        print("(", end="")
        checkQuadTree(n, y, x)
        checkQuadTree(n, y, x+n)
        checkQuadTree(n, y+n, x)
        checkQuadTree(n, y+n, x+n)
        print(")", end="")

N = int(sys.stdin.readline())
video = [sys.stdin.readline().rstrip() for _ in range(N)]
checkQuadTree(N, 0, 0)