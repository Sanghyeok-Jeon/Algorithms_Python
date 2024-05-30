import sys
import collections

def BFS(i, j):
    q = collections.deque()
    q.append((i, j))
    targetColor = grd[i][j]

    while q:
        x, y = q.popleft()
        visited[x][y] = 1
        if x+1 < N and (x+1, y) not in q and not visited[x+1][y] and grd[x+1][y] == targetColor:
            q.append((x+1, y))
        if x-1 >= 0 and (x-1, y) not in q and not visited[x-1][y] and grd[x-1][y] == targetColor:
            q.append((x-1, y))
        if y+1 < N and (x, y+1) not in q and not visited[x][y+1] and grd[x][y+1] == targetColor:
            q.append((x, y+1))
        if y-1 >= 0 and (x, y-1) not in q and not visited[x][y-1] and grd[x][y-1] == targetColor:
            q.append((x, y-1))
    return

N = int(sys.stdin.readline())
grd = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

normal = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            BFS(i, j)
            normal += 1

for i in range(N):
    for j in range(N):
        if grd[i][j] == 'R':
            grd[i][j] = 'G'

visited = [[0] * N for _ in range(N)]
weakColor = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            BFS(i, j)
            weakColor += 1

print(normal, weakColor)