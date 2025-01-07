import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))

cnt = 0
for i in range(N - 1, 0, -1):
    for j in range(i):
        if A[j] > A[j + 1]:
            A[j], A[j + 1] = A[j + 1], A[j]
            cnt += 1
            if cnt == K:
                print(A[j], A[j + 1])
                exit(0)

print(-1)