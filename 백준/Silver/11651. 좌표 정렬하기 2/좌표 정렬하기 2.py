import sys

N = int(sys.stdin.readline())
coordinate = []
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    coordinate.append((x, y))

coordinate.sort(key=lambda x:(x[1], x[0]))

for xy in coordinate:
    print('{} {}'.format(xy[0], xy[1]))