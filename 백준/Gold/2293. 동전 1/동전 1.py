n, k = map(int, input().split())
coin = [0] + [int(input()) for _ in range(n)]
dp = [0] * (k+1)
dp[0] = 1

for i in range(1, n+1):
    for j in range(coin[i], k+1):
        dp[j] += dp[j-coin[i]]

print(dp[k])