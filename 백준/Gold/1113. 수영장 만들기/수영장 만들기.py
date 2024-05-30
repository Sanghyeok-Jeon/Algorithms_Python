from collections import deque
import sys

def bfs(x, y, n):
    global result, visited

    q = deque([(x, y)])
    visited[x][y] = 1
    cnt = 1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    possible = True    # 수영장 가능 여부 체크
    while q:
        x, y = q.popleft()
        for mode in range(4):
            nx = x + dx[mode]
            ny = y + dy[mode]
            # 수영장 안되는 곳 나오면 불가능으로 바꾸고 연결된 부분 전부 체크
            if nx == -1 or nx == N or ny == -1 or ny == M:
                possible = False
                continue

            # 수영장 되든 안되든 연결된 부분 모두 체크하는 부분
            if board[nx][ny] <= n and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                q.append((nx, ny))
                cnt += 1

    if possible:
        result += cnt

    return

N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(N)]

result = 0
for num in range(1, 9):    # 수면 1부터 상승
    visited = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if board[i][j] <= num and visited[i][j] == 0:    # 물을 채울 수 있는 곳
                bfs(i, j, num)

print(result)