dp = [0] * 100001
dp[1], dp[2], dp[3], dp[4], dp[5], dp[6] = 1, 2, 2, 3, 3, 6
for i in range(7, 100001):
    dp[i] = (dp[i-2] + dp[i-4] + dp[i-6]) % 1000000009

T = int(input())
for tc in range(T):
    n = int(input())
    print(dp[n])