def draw_star(n, x, y):
    if n == 1:
        stars[y][x] = '*'
        stars[y + 1][x] = '*'
        stars[y + 2][x] = '*'
    else:
        for i in range(4 * n - 4):
            stars[y][x] = '*'
            x -= 1

        for i in range(4 * n - 2):
            stars[y][x] = '*'
            y += 1

        for i in range(4 * n - 4):
            stars[y][x] = '*'
            x += 1

        for i in range(4 * n - 4):
            stars[y][x] = '*'
            y -= 1

        stars[y][x] = '*'
        stars[y][x - 1] = '*'

        draw_star(n - 1, x - 2, y)

N = int(input())

w = 4 * N - 3
h = 4 * N - 1

stars = [[' ' for _ in range(w)] for _ in range(h)]

if N == 1:
    print('*')
else:
    draw_star(N, w - 1, 0)

    for star in stars:
        print(''.join(star).rstrip())