from collections import deque
import sys
input = sys.stdin.readline

def bfs(sx, sy):
    q = deque()
    total_cnt = -1
    q.append((sx, sy, 0))
    visited[sx][sy][0] = 1

    while q:
        x, y, key = q.popleft()

        if board[x][y] == '1':
            total_cnt = visited[x][y][key] - 1
            break

        for mode in range(4):
            nx = x + dx[mode]
            ny = y + dy[mode]
            # 범위 안이고 벽이 아니면서 동일한 키로 방문한 적이 없는 경우
            if 0 <= nx < N and 0 <= ny < M and board[nx][ny] != '#' and visited[nx][ny][key] == 0:
                # 열쇠인 경우
                if board[nx][ny].islower():
                    nkey = key | (1 << (ord(board[nx][ny]) - ord('a')))
                    if visited[nx][ny][nkey] == 0:
                        visited[nx][ny][nkey] = visited[x][y][key] + 1
                        q.append((nx, ny, nkey))
                # 문인 경우
                elif board[nx][ny].isupper():
                    if key & (1 << (ord(board[nx][ny]) - ord('A'))):
                        visited[nx][ny][key] = visited[x][y][key] + 1
                        q.append((nx, ny, key))
                # 길인 경우
                else:
                    visited[nx][ny][key] = visited[x][y][key] + 1
                    q.append((nx, ny, key))

    return total_cnt

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[[0] * 64 for _ in range(M)] for _ in range(N)]

start_x, start_y = 0, 0
for i in range(N):
    for j in range(M):
        if board[i][j] == '0':
            start_x, start_y = i, j

print(bfs(start_x, start_y))