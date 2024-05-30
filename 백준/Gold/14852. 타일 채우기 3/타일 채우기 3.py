N = int(input())
dp = [[0, 0] for _ in range(N+1)]
dp[0][0] = 1

for i in range(1, N+1):
    if i == 1:
        dp[i][0] = 2
    elif i == 2:
        dp[i][0] = 7
    else:
        dp[i][1] = (dp[i-1][1] + dp[i-3][0]) % 1000000007
        dp[i][0] = (dp[i-1][0] * 2 + dp[i-2][0] * 3 + dp[i][1] * 2) % 1000000007

print(dp[N][0])