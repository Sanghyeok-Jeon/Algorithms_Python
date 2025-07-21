N = int(input())
M = int(input())
xy = [tuple(map(int, input().split())) for _ in range(M)]

rooms = [0] + [1] * N

for x, y in xy:
    for i in range(x, y):
        rooms[i] = 0

print(sum(rooms))