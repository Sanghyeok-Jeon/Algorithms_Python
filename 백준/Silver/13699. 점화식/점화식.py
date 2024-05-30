n = int(input())

dp = [0] * 36

for i in range(n+1):
    if i == 0:
        dp[i] = 1
    else:
        dp[i] = 0
        for j in range(i):
            dp[i] += dp[j] * dp[i-1-j]

print(dp[n])