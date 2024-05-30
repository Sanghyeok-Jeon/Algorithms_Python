T = int(input())
for tc in range(T):
    k, n = int(input()), int(input())
    dp = [[0]*(n+1) for _ in range(k+1)]
    for i in range(1, n+1):
        dp[0][i] = i + dp[0][i-1]

    for i in range(1, k):
        for j in range(1, n+1):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

    print(dp[k-1][n])