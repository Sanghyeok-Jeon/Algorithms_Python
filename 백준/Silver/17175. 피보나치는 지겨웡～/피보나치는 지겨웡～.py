n = int(input())

dp = [0] * (n+1)
for i in range(n+1):
    if i < 2:
        dp[i] = 1
    else:
        dp[i] = (dp[i-1] + dp[i-2] + 1) % 1000000007

print(dp[n])