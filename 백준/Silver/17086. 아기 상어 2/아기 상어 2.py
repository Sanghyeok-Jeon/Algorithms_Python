from collections import deque

def bfs(n, m, grid):
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    queue = deque()
    distance = [[-1] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                queue.append((i, j))
                distance[i][j] = 0

    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and distance[nx][ny] == -1:
                distance[nx][ny] = distance[x][y] + 1
                queue.append((nx, ny))

    max_distance = 0
    for i in range(n):
        for j in range(m):
            if distance[i][j] > max_distance:
                max_distance = distance[i][j]

    return max_distance

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
result = bfs(n, m, grid)
print(result)