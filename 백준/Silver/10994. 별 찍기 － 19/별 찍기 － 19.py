def draw_stars(n, x, y):
    if n == 1:
        stars[y][x] = '*'
        return

    length = 4 * n - 3

    for i in range(length):
        stars[y][x + i] = '*'

    for i in range(length):
        stars[y + length - 1][x + i] = '*'

    for i in range(length):
        stars[y + i][x] = '*'

    for i in range(length):
        stars[y + i][x + length - 1] = '*'

    draw_stars(n - 1, x + 2, y + 2)

N = int(input())

size = 4 * (N - 1) + 1
stars = [[' '] * size for _ in range(size)]

draw_stars(N, 0, 0)

for row in stars:
    print(''.join(row))

