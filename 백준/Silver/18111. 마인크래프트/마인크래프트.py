import sys

N, M, B = map(int, sys.stdin.readline().split())
field = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
time = 256 * N * M + 1
height = 0
MAX, MIN = max(map(max, field)), min(map(min, field))

for f in range(MIN, MAX+1):
    fieldUp, fieldDown = 0, 0
    for j in range(N):
        for k in range(M):
            if field[j][k] < f:
                fieldUp += f - field[j][k]
            else:
                fieldDown += field[j][k] - f
    inventory = fieldDown + B
    if inventory >= fieldUp:
        tempTime = 2 * fieldDown + fieldUp
        if tempTime <= time:
            time = tempTime
            height = f

print(time, height)