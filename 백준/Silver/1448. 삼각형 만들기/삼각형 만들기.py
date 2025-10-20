import sys
input = sys.stdin.readline

N = int(input())
sides = [int(input()) for _ in range(N)]
sides.sort()

for i in range(N - 1, 1, -1):
    if sides[i] < sides[i - 1] + sides[i - 2]:
        print(sides[i] + sides[i - 1] + sides[i -2])
        break
else:
    print(-1)