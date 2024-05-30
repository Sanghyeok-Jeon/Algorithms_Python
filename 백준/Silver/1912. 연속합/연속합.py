n = int(input())
dp = [0] + list(map(int, input().split()))

ans = -1000 * n
for i in range(1, n+1):
    dp[i] = max(dp[i-1]+dp[i], dp[i])
    if dp[i] > ans:
        ans = dp[i]

print(ans)