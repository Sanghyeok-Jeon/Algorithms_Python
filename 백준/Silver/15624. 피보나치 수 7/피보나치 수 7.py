n = int(input())
dp = [0] * (n+1)
for i in range(n+1):
    if i == 0:
        dp[i] = 0
    elif i == 1:
        dp[i] = 1
    else:
        dp[i] = (dp[i-1] + dp[i-2]) % 1000000007

print(dp[n] % 1000000007)