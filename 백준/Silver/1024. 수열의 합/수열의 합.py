import sys

N, L = map(int, sys.stdin.readline().rstrip().split())
ans = -1
length = 0

for l in range(L, 101):
    tmp = l * (l - 1) // 2
    if not (N - tmp) % l and (N - tmp) // l >= 0:
        ans = (N - tmp) // l
        length = l
        break

if ans == -1:
    print(-1)
else:
    for i in range(length):
        print(ans + i, end=' ')
