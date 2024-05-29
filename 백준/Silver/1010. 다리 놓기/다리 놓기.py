T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    dp = [[0]*(M+1) for i in range(N+1)]
    for n in range(N+1):
        for m in range(n, M+1):
            if n < 2:
                dp[n][m] = n*m
            else:
                dp[n][m] = dp[n-1][m-1] + dp[n][m-1]

    print(dp[N][M])