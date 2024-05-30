N = int(input())

dp = [[0, 0] for _ in range(N+1)]
for i in range(1, N+1):
    if i == 1:
        dp[i][0], dp[i][1] = 1, 4
    else:
        dp[i][0] = dp[i-1][0] + dp[i-2][0]
        dp[i][1] = 2 * (dp[i-1][0] + dp[i][0] + dp[i][0])

print(dp[N][1])