import sys
sys.setrecursionlimit(100000)

def DFS(i, j):
    if i < 0 or i >= N or j < 0 or j >= M or board[i][j] == 'H':
        return 0
    if visited[i][j]:
        print(-1)
        exit()
    if dp[i][j] != -1:
        return dp[i][j]

    visited[i][j] = 1
    for mode in range(4):
        dp[i][j] = max(dp[i][j], DFS(i+int(board[i][j])*di[mode], j+int(board[i][j])*dj[mode])+1)
    visited[i][j] = 0
    return dp[i][j]


N, M = map(int, input().split())
board = [input() for _ in range(N)]
visited = [[0]*M for _ in range(N)]
dp = [[-1]*M for _ in range(N)]

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

print(DFS(0, 0))