T = int(input())

dp = [0] * 1000001
dp[1], dp[2], dp[3] = 1, 2, 4
for i in range(4, 1000001):
    dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % 1000000009

for tc in range(T):
    n = int(input())
    print(dp[n])