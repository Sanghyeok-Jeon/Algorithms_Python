import sys
N = int(sys.stdin.readline())
cost = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [[0, 0, 0] for _ in range(N)]

for i in range(N):
    if i == 0:
        dp[i] = cost[i]
    else:
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + cost[i][0]
        dp[i][1] = min(dp[i-1][2], dp[i-1][0]) + cost[i][1]
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + cost[i][2]

print(min(dp[N-1]))