import sys
input = sys.stdin.readline

n = int(input().strip())

dp = [i for i in range(n + 1)]

for i in range(1, n + 1):
    j = 1
    while j * j <= i:
        square = j * j
        if dp[i] > dp[i - square] + 1:
            dp[i] = dp[i - square] + 1
        j += 1

print(dp[n])