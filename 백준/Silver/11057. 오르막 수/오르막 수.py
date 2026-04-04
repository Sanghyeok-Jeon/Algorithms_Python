import sys

input = sys.stdin.readline
MOD = 10007

n = int(input())

dp = [[0] * 10 for _ in range(n + 1)]

for j in range(10):
    dp[1][j] = 1

for i in range(2, n + 1):
    for j in range(10):
        for k in range(j + 1):
            dp[i][j] += dp[i - 1][k]
        dp[i][j] %= MOD

print(sum(dp[n]) % MOD)