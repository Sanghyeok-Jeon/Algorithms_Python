while True:
    try:
        N = int(input())
        dp = [0] * (N+1)
        for i in range(N+1):
            if i == 0:
                dp[i] = 1
            elif i == 1:
                dp[i] = 1
            elif i == 2:
                dp[i] = 3
            else:
                dp[i] = dp[i-2] * 2 + dp[i-1]
        print(dp[N])
    except:
        break