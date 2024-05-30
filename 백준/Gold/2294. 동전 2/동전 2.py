n, k = map(int, input().split())
coin = [0] + [int(input()) for _ in range(n)]

dp = [0] + [10001] * k

for i in range(1, n+1):
    for j in range(coin[i], k+1):
        dp[j] = min(dp[j], dp[j-coin[i]]+1)

print(dp[k] if dp[k] != 10001 else -1)