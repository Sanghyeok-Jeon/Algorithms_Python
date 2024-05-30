R, C, ZR, ZC = map(int, input().split())
newspaper = [input() for _ in range(R)]
scan = [['']*C*ZC for _ in range(R*ZR)]

for r in range(0, R*ZR, ZR):
    for c in range(0, C*ZC, ZC):
        expand = newspaper[r//ZR][c//ZC]
        for sr in range(r, r+ZR):
            for sc in range(c, c+ZC):
                scan[sr][sc] = expand

for i in range(R*ZR):
    print(''.join(scan[i]))