N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

M, K = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(M)]

xMatrix = [[0 for _ in range(K)] for _ in range(N)]
for n in range(N):
    for k in range(K):
        for m in range(M):
            xMatrix[n][k] += A[n][m] * B[m][k]

for n in range(N):
    print(*xMatrix[n])