from collections import deque

def BFS():
    while q:
        i, j, d = q.popleft()
        if visited[i][j]:
            continue

        visited[i][j] = True

        for mode in range(4):
            ni = i + di[mode]
            nj = j + dj[mode]

            if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj]:
                if land[ni][nj] == 1:
                    distance[ni][nj] = d + 1
                    q.append((ni, nj, d+1))

n, m = map(int, input().split())
land = [list(map(int, input().split())) for _ in range(n)]
distance = [[-1] * m for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]

x, y = 0, 0
for i in range(n):
    for j in range(m):
        if land[i][j] == 0:
            distance[i][j] = 0
        if land[i][j] == 2:
            x, y = i, j

distance[x][y] = 0
q = deque()
q.append((x, y, 0))
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

BFS()

for i in range(n):
    print(*distance[i])