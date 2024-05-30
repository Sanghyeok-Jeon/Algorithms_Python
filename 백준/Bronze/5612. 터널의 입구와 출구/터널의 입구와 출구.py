n = int(input())
m = int(input())

maxCnt = m
for _ in range(n):
    i, o = map(int, input().split())
    m += i - o

    if m < 0:
        maxCnt = 0
        break

    maxCnt = max(maxCnt, m)

print(maxCnt)