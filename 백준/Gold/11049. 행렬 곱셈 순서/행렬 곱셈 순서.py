import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * N for _ in range(N)]

for term in range(1, N):
    for start in range(N - term):
        dp[start][start + term] = int(1e9)

        for t in range(start, start + term):
            tmp = dp[start][t] + dp[t+1][start + term] + arr[start][0] * arr[t][1] * arr[start + term][1]
            dp[start][start + term] = min(dp[start][start + term], tmp)

print(dp[0][N - 1])