import sys

input = sys.stdin.readline
N = int(input().strip())
D = []
for _ in range(N):
    A, B = map(int, input().split())
    D.append(B - A)

D.sort()

if N % 2 == 1:
    print(1)
else:
    left = D[N//2 - 1]
    right = D[N//2]
    print(right - left + 1)