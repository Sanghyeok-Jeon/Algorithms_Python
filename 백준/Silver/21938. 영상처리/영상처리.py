import sys
from collections import deque

input = sys.stdin.readline

# 방향 벡터 (우, 하, 좌, 상)
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

N, M = map(int, input().split())

# RGB가 3개씩 붙어서 들어오므로, 한 줄에 3*M개의 숫자가 들어온다.
screen = [[0] * M for _ in range(N)]

for i in range(N):
    row = list(map(int, input().split()))  # 길이 3*M
    for j in range(M):
        r = row[3 * j]
        g = row[3 * j + 1]
        b = row[3 * j + 2]
        avg = (r + g + b) // 3
        screen[i][j] = avg

T = int(input())

# 이진화: avg >= T 이면 255, 아니면 0
for i in range(N):
    for j in range(M):
        if screen[i][j] >= T:
            screen[i][j] = 255
        else:
            screen[i][j] = 0

visited = [[False] * M for _ in range(N)]

def bfs(sx, sy):
    q = deque()
    q.append((sx, sy))
    visited[sx][sy] = True

    while q:
        x, y = q.popleft()
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny] and screen[nx][ny] == 255:
                    visited[nx][ny] = True
                    q.append((nx, ny))

cnt = 0
for i in range(N):
    for j in range(M):
        if screen[i][j] == 255 and not visited[i][j]:
            bfs(i, j)
            cnt += 1

print(cnt)