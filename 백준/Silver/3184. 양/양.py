import sys
import collections

def BFS():
    global sum_sheep, sum_wolf
    sheep, wolf = 0, 0
    while q:
        i, j = q.popleft()
        for mode in range(4):
            ni = i + di[mode]
            nj = j + dj[mode]
            if 0 <= ni < R and 0 <= nj < C and visited[ni][nj] == 0 and data[ni][nj] != '#':
                visited[ni][nj] = 1
                q.append((ni, nj))
                if data[ni][nj] == 'o':
                    sheep += 1
                if data[ni][nj] == 'v':
                    wolf += 1
    if sheep > wolf:
        sum_sheep += sheep
    else:
        sum_wolf += wolf
    return

R, C = map(int, sys.stdin.readline().split())
data = [list(input()) for _ in range(R)]
q = collections.deque()
visited = [[0]*C for _ in range(R)]
sum_sheep, sum_wolf = 0, 0

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

for i in range(R):
    for j in range(C):
        if visited[i][j] == 0:
            if data[i][j] == '.' or 'o' or 'v':
                visited[i][j] = 1
                q.append((i, j))
                BFS()

print(sum_sheep, sum_wolf)