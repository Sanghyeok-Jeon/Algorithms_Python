import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs(x, y):
    if x == N - 1 and y == M - 1:
        return 1

    if dp[x][y] > -1:
        return dp[x][y]

    dp[x][y] = 0
    for mode in range(4):
        nx = x + dx[mode]
        ny = y + dy[mode]

        if 0 <= nx < N and 0 <= ny < M and map_num[nx][ny] < map_num[x][y]:
            dp[x][y] += dfs(nx, ny)

    return dp[x][y]

N, M = map(int, input().split())
map_num = [list(map(int, input().split())) for _ in range(N)]
dp = [[-1] * M for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(dfs(0, 0))