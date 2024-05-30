N, M, L = map(int, input().split())

cntDict = {}
for i in range(1, N+1):
    cntDict[i] = 0

totalCnt = 0
i = 1
while True:
    cntDict[i] += 1
    totalCnt += 1
    nowCnt = cntDict[i]

    if nowCnt == M:
        break

    if nowCnt % 2:
        i += L
        if i > N:
            i -= N
    else:
        i -= L
        if i < 1:
            i += N

print(totalCnt - 1)