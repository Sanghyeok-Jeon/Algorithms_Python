import sys
input = sys.stdin.readline

N = int(input())
max_y = -(10 ** 9 + 1)
min_y = 10 ** 9 + 1
for _ in range(N):
    x, y = map(int, input().split())

    max_y = max(max_y, y)
    min_y = min(min_y, y)

print(max_y - min_y)