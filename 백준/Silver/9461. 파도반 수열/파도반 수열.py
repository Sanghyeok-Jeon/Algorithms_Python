T = int(input())

for tc in range(T):
    N = int(input())
    dp = [0] * 101

    for i in range(1, N+1):
        if i < 4:
            dp[i] = 1
        elif 4 <= i < 6:
            dp[i] = 2
        else:
            dp[i] = dp[i-1] + dp[i-5]

    print(dp[N])