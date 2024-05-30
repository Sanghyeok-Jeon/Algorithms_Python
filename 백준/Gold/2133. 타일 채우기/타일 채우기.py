N = int(input())

dp = [0] * (N+1)

dp[0] = 1
for i in range(2, N+1, 2):
    if i == 2:
        dp[i] = 3
    else:
        dp[i] += dp[i-2] * 3
        for j in range(i-4, -1, -2):
            dp[i] += dp[j] * 2
dp[0] = 0

print(dp[N])