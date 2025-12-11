def find_seat_position(C, R, K):
    if K > C * R:
        return 0, 0

    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    seats = [[0]* C for _ in range(R)]
    x, y = 0, 0
    direction = 0
    count = 1

    while count < K:
        seats[y][x]= count
        nx, ny = x + directions[direction][1], y + directions[direction][0]

        if 0 <= nx < C and 0 <= ny < R and seats[ny][nx]== 0:
            x, y = nx, ny
        else:
            direction = (direction + 1) % 4
            x += directions[direction][1]
            y += directions[direction][0]

        count += 1

    return x + 1, y + 1

import sys
input = sys.stdin.readline

C, R = map(int, input().split())
K = int(input())

x, y = find_seat_position(C, R, K)
if x == 0 and y == 0:
    print(0)
else:
    print(x, y)