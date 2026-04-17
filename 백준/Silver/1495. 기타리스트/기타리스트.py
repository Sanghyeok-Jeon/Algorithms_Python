import sys

input = sys.stdin.readline

n, s, m = map(int, input().split())
arr = list(map(int, input().split()))

dp = [[False] * (m + 1) for _ in range(n + 1)]
dp[0][s] = True

for i in range(n):
    for v in range(m + 1):
        if dp[i][v]:
            if v + arr[i] <= m:
                dp[i + 1][v + arr[i]] = True
            if v - arr[i] >= 0:
                dp[i + 1][v - arr[i]] = True

for v in range(m, -1, -1):
    if dp[n][v]:
        print(v)
        break
else:
    print(-1)