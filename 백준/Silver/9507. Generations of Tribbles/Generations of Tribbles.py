dp = [1, 1, 2, 4] + [0] * 66
for i in range(4, 70):
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3] + dp[i - 4]

t = int(input())
for _ in range(t):
    n = int(input())
    print(dp[n])