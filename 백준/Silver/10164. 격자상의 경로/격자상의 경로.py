import sys

def count_paths(a, b):
    dp = [[0] * (b + 1) for _ in range(a + 1)]
    dp[1][1] = 1
    for i in range(1, a + 1):
        for j in range(1, b + 1):
            if i == 1 and j == 1:
                continue
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[a][b]

input = sys.stdin.readline
N, M, K = map(int, input().split())

if K == 0:
    print(count_paths(N, M))
    exit(0)
    
r = (K - 1) // M + 1
c = (K - 1) % M + 1

ans = count_paths(r, c) * count_paths(N - r + 1, M - c + 1)
print(ans)