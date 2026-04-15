import sys

input = sys.stdin.readline

n, d = map(int, input().split())
shortcuts = []

for _ in range(n):
    start, end, dist = map(int, input().split())
    if end <= d and end - start > dist:
        shortcuts.append((start, end, dist))

dp = [0] * (d + 1)

for i in range(1, d + 1):
    dp[i] = dp[i - 1] + 1
    for start, end, dist in shortcuts:
        if end == i:
            dp[i] = min(dp[i], dp[start] + dist)

print(dp[d])