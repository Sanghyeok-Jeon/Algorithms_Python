n, m = map(int, input().split())
data = [list(map(int, input())) for _ in range(n)]

dp = [[0]*(m+1) for _ in range(n+1)]
    
maxCnt = 0
for i in range(1, n+1):
    for j in range(1, m+1):
        if data[i-1][j-1]:
            dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1
            maxCnt = max(dp[i][j], maxCnt)

print(maxCnt ** 2)