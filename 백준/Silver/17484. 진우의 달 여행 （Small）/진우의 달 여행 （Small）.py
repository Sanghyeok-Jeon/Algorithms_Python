import sys
input = sys.stdin.readline
INF = 10**9

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dp = [[[INF] * 3 for _ in range(M)] for _ in range(N)]

for c in range(M):
    for d in range(3):
        dp[0][c][d] = board[0][c]

dc = [-1, 0, 1]

for r in range(1, N):
    for c in range(M):
        for d in range(3):
            prev_c = c - dc[d]
            if 0 <= prev_c < M:
                for pd in range(3):
                    if pd == d:
                        continue
                    if dp[r-1][prev_c][pd] == INF:
                        continue
                    dp[r][c][d] = min(dp[r][c][d], dp[r-1][prev_c][pd] + board[r][c])

answer = INF
for c in range(M):
    for d in range(3):
        answer = min(answer, dp[N-1][c][d])

print(answer)
