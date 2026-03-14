N, M = map(int, input().split())
land = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if i == 0 and j == 0:
            dp[i][j] = land[i][j]
        else:
            if j - 1 >= 0 and i - 1 >= 0:
                dp[i][j] = max(dp[i][j - 1] + land[i][j], dp[i - 1][j] + land[i][j])
            elif i - 1 >= 0:
                dp[i][j] = dp[i - 1][j] + land[i][j]
            elif j - 1 >= 0:
                dp[i][j] = dp[i][j - 1] + land[i][j]

print(dp[N-1][M-1])