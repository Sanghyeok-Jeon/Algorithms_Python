import sys
sys.setrecursionlimit(1000000000)

def DFS(i, j):
    if dp[i][j]:
        return dp[i][j]
    else:
        dp[i][j] = 1

    for mode in range(4):
        ni = i + di[mode]
        nj = j + dj[mode]
        if 0 <= ni < n and 0 <= nj < n and bamboo[ni][nj] > bamboo[i][j]:
            dp[i][j] = max(dp[i][j], DFS(ni, nj)+1)

    return dp[i][j]

n = int(input())
bamboo = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]
di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

maxDay = 0
for i in range(n):
    for j in range(n):
        maxDay = max(maxDay, DFS(i, j))

print(maxDay)