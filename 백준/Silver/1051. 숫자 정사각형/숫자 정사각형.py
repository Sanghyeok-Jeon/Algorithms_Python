N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
max_len = min(N, M)
answer = 1

for k in range(max_len):
    for i in range(N - k):
        for j in range(M - k):
            if arr[i][j] == arr[i][j + k] == arr[i + k][j] == arr[i + k][j + k]:
                answer = max(answer, (k + 1) ** 2)

print(answer)