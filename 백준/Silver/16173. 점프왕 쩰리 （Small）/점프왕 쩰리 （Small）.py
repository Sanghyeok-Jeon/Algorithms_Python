from collections import deque

def bfs():
    q = deque([(0, 0)])

    while q:
        x, y = q.popleft()
        num = board[x][y]

        if board[x][y] == -1:
            return True

        for mode in range(2):
            nx = x + dx[mode] * num
            ny = y + dy[mode] * num

            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                visited[nx][ny] = 1
                q.append((nx, ny))

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

visited = [[0] * N for _ in range(N)]

dx = [1, 0]
dy = [0, 1]

print('HaruHaru' if bfs() else 'Hing')
