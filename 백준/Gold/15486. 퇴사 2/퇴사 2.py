import sys

input = sys.stdin.readline
N = int(input())
dp = [0] * (N+1)

max_now = 0
for i in range(N):
    T, P = map(int, input().split())
    max_now = max(max_now, dp[i])
    
    if i + T <= N:
        if dp[i+T] < max_now + P:
            dp[i+T] = max_now + P

print(max(dp))