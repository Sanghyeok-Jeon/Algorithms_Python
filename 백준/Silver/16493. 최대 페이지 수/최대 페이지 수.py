import sys
input = sys.stdin.readline

N, M = map(int, input().split())

chapters = []
for _ in range(M):
    d, p = map(int, input().split())
    chapters.append((d, p))

dp = [0] * (N + 1)

for d, p in chapters:
    for days in range(N, d - 1, -1):
        dp[days] = max(dp[days], dp[days - d] + p)

print(dp[N])