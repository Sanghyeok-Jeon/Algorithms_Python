N = int(input())
dp = [0] * 21

for i in range(1, N+1):
    T, P = map(int, input().split())
    dp[i+1] = max(dp[i], dp[i+1])
    if i + T <= N+1:
        dp[i + T] = max(dp[i] + P, dp[i + T])

print(max(dp))