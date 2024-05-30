def spot(x, y, n):
    if n == 1:
        star[x][y] = '*'
        return

    new_n = n//3
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            spot(x+new_n*i, y+new_n*j, new_n)

N = int(input())
star = [[' 'for i in range(N)] for _ in range(N)]

spot(0, 0, N)

for s in star:
    print(''.join(s))