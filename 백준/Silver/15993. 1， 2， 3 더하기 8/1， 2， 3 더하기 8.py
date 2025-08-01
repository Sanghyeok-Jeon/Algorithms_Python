dp = [[0, 0] for _ in range(100000 + 1)]  # dp[i][0] : odd, dp[i][1] : even
for i in range(1, 100000 + 1):
    if i == 1:
        dp[i][0] = 1
    elif i == 2:
        dp[i][0] = 1
        dp[i][1] = 1
    elif i == 3:
        dp[i][0] = 2
        dp[i][1] = 2
    else:
        dp[i][0] = (dp[i - 1][1] + dp[i - 2][1] + dp[i - 3][1]) % 1000000009
        dp[i][1] = (dp[i - 1][0] + dp[i - 2][0] + dp[i - 3][0]) % 1000000009

T = int(input())
for tc in range(T):
    n = int(input())
    print(*dp[n])