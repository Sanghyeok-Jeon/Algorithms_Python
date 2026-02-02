import sys

MOD = 1_000_000_007

input = sys.stdin.readline
N, M = map(int, input().split())

dp = [0] * (N + 1)
dp[0]= 1

for t in range(1, N + 1):
    dp[t] = dp[t - 1]
    if t >= M:
        dp[t] = (dp[t] + dp[t - M]) % MOD
    else:
        dp[t] %= MOD

print(dp[N]% MOD)