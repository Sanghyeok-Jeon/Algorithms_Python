import sys

input = sys.stdin.readline
n, m = map(int, input().split())

trains = [0] * (n + 1)
mask20 = (1 << 20) - 1

for _ in range(m):
    cmd = list(map(int, input().split()))
    t = cmd[0]

    if t == 1:
        i, x = cmd[1], cmd[2]
        trains[i] |= (1 << (x - 1))

    elif t == 2:
        i, x = cmd[1], cmd[2]
        trains[i] &= ~(1 << (x - 1))

    elif t == 3:
        i = cmd[1]
        trains[i] = (trains[i] << 1) & mask20

    else:
        i = cmd[1]
        trains[i] >>= 1

print(len(set(trains[1:])))