N, M = map(int, input().split())
A = list(map(int, input().split()))

stress = 0
cnt = 0
for i in range(N):
    if A[i] >= 0:
        stress += A[i]
    else:
        stress = max(0, stress + A[i])

    if stress >= M:
        cnt += 1

print(cnt)
