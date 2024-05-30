import sys
import collections

def BFS():
    global N, M, visited
    while q:
        i, j = q.popleft()
        for mode in range(4):
            ni = i + di[mode]
            nj = j + dj[mode]
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0 and maze[ni][nj] == '1':
                visited[ni][nj] = visited[i][j] + 1
                q.append((ni, nj))

    return visited[N-1][M-1]

N, M = map(int, sys.stdin.readline().split())
maze = [list(input()) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
q = collections.deque()

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

q.append((0, 0))
visited[0][0] = 1

print(BFS())