import sys
input = sys.stdin.readline

INF = float('inf')

N = int(input())
A = list(map(int, input().split()))
dp = [-INF, -INF, -INF, -INF]

for i in range(N):
    dp[3] = max(dp[3], dp[2] + A[i])
    dp[2] = max(dp[2], dp[1] - A[i])
    dp[1] = max(dp[1], dp[0] + A[i])
    dp[0] = max(dp[0], -A[i])

print(dp[3])