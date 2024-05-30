N = int(input())
data = list(map(int, input().split()))

dp = [1000] * N
for i in range(N):
    if i == 0:
        dp[i] = 0
    for j in range(1, data[i]+1):
        if i+j >= N:
            break
        dp[i+j] = min(dp[i+j], dp[i]+1)

print(dp[N-1] if dp[N-1] != 1000 else -1)