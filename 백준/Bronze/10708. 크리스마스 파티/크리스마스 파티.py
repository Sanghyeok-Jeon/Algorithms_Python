N = int(input())
M = int(input())
A = list(map(int, input().split()))

score = [0] * N
for i in range(M):
    B = list(map(int, input().split()))
    failCnt = 0
    for j in range(N):
        if B[j] == A[i]:
            score[j] += 1
        else:
            failCnt += 1

    score[A[i] - 1] += failCnt

for i in range(N):
    print(score[i])
