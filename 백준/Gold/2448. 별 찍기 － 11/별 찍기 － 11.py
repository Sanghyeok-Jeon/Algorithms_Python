def printStar(x, y, n):
    if n == 3:
        result[x][y] = '*'
        result[x+1][y-1] = result[x+1][y+1] = '*'
        for i in range(-2, 3):
            result[x+2][y+i] = '*'
    else:
        half_n = n // 2
        printStar(x, y, half_n)
        printStar(x+half_n, y-half_n, half_n)
        printStar(x+half_n, y+half_n, half_n)

N = int(input())
result = [[' ']*2*N for _ in range(N)]

printStar(0, N-1, N)

for rs in result:
    print(''.join(rs))