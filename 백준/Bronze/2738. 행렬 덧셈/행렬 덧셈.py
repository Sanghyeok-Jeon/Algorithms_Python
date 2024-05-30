N, M = map(int, input().split())

result = [[0] * M for _ in range(N)]
for _ in range(2):
    for n in range(N):
        tmpColumn = list(map(int, input().split()))
        for m in range(M):
            result[n][m] += tmpColumn[m]

for i in range(N):
    print(*result[i])