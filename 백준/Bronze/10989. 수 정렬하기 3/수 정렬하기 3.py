import sys

N = int(sys.stdin.readline())
cntNum = [0] * 10001
for n in sys.stdin:
    cntNum[int(n)] += 1

cnt = 0
for i in range(1, 10001):
    if cntNum[i]:
        for _ in range(cntNum[i]):
            print(i)
            cnt += 1

    if cnt == N:
        break