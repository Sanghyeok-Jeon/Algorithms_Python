N = int(input())
stair = [0]
for _ in range(N):
    stair.append(int(input()))

dp = [0] * (N+1)
for i in range(1, N+1):
    if i == 1:
        dp[i] = stair[i]
    elif i == 2:
        dp[i] = stair[i] + dp[i-1]
    else:
        dp[i] = max(stair[i] + dp[i-2], stair[i] + stair[i-1] + dp[i-3])

print(dp[N])