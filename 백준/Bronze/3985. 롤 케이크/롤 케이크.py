L = int(input())
N = int(input())

cake = [0] * (L + 1)
maxCnt = 0
cakeCnt = [0] * (N + 1)
for n in range(1, N+1):
    P, K = map(int, input().split())

    cnt = K - P + 1
    if cnt > maxCnt:
        maxCnt = cnt
        maxNo = n

    for i in range(P, K+1):
        if not cake[i]:
            cake[i] = n
            cakeCnt[n] += 1

print(maxNo)
print(cakeCnt.index(max(cakeCnt)))
