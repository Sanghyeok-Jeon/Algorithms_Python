import sys

sys.setrecursionlimit(1000000)

def DFS(x, y):
    global cntMeet

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    for mode in range(4):
        nx = x + dx[mode]
        ny = y + dy[mode]
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            if campus[nx][ny] == 'O':
                visited[nx][ny] = True
                DFS(nx, ny)
            elif campus[nx][ny] == 'X':
                continue
            elif campus[nx][ny] == 'P':
                cntMeet += 1
                visited[nx][ny] = True
                DFS(nx, ny)

N, M = map(int, input().split())
campus = [input() for _ in range(N)]
visited = [[False]*M for _ in range(N)]

startX, startY = 0, 0
for i in range(N):
    for j in range(M):
        if campus[i][j] == 'I':
            startX, startY = i, j
            visited[i][j] = True

cntMeet = 0
DFS(startX, startY)

print(cntMeet if cntMeet else 'TT')