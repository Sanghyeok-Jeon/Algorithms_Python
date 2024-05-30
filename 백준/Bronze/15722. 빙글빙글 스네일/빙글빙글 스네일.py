def move_snail(x, y, sec):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    mode = 0
    length = 1
    changeDirection = 0
    while True:
        for _ in range(length):
            if sec == n:
                return x, y

            x += dx[mode]
            y += dy[mode]

            sec += 1

        changeDirection += 1
        mode = (mode + 1) % 4

        if changeDirection == 2:
            length += 1
            changeDirection = 0

n = int(input())
print(*move_snail(0, 0, 0))