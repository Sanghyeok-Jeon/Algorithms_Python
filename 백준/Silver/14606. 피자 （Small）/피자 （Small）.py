N = int(input())

dp = [0] * (N + 1)
for i in range(N+1):
    if i == 1:
        dp[i] = 0
    elif i == 2:
        dp[i] = 1
    else:
        half = i // 2
        dp[i] = half * (i - half) + dp[half] + dp[i - half]

print(dp[N])