import sys

input = sys.stdin.readline

R, C, K = map(int, input().split())
board = [list(input().strip()) for _ in range(R)]

visited = [[False] * C for _ in range(R)]
answer = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y, dist):
    global answer

    if x == 0 and y == C - 1:
        if dist == K:
            answer += 1
        return

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < R and 0 <= ny < C:
            if not visited[nx][ny] and board[nx][ny] != 'T':
                visited[nx][ny] = True
                dfs(nx, ny, dist + 1)
                visited[nx][ny] = False


start_x, start_y = R - 1, 0
visited[start_x][start_y] = True
dfs(start_x, start_y, 1)

print(answer)