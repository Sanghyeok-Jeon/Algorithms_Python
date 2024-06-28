from collections import deque
import sys
input = sys.stdin.readline

def bfs(N, M, K, grid):
    # 방향 벡터 (상, 하, 좌, 우)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    # 방문 체크 배열: [x][y][벽을 부순 횟수]
    visited = [[[False] * (K + 1) for _ in range(M)]for _ in range(N)]

    # 큐 초기화: (x, y, 벽을 부순 횟수, 낮/밤, 이동 횟수)
    queue = deque([(0, 0, 0, 1)])  # 낮은 1, 밤은 0
    visited[0][0][0] = True

    while queue:
        x, y, broken, dist = queue.popleft()
        day = dist % 2

        # 목적지 도달 체크
        if x == N - 1 and y == M - 1:
            return dist

        # 4방향 탐색
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < N and 0 <= ny < M:
                # 벽이 아닌 경우
                if grid[nx][ny] == '0' and not visited[nx][ny][broken]:
                    visited[nx][ny][broken] = True
                    queue.append((nx, ny, broken, dist + 1))

                # 벽인 경우
                if grid[nx][ny] == '1' and broken < K and not visited[nx][ny][broken + 1]:
                    if day:
                        visited[nx][ny][broken + 1] = True
                        queue.append((nx, ny, broken + 1, dist + 1))
                    else:
                        visited[x][y][broken] = True
                        queue.append((x, y, broken, dist + 1))

    return -1

N, M, K = map(int, input().split())
grid = [input().rstrip() for _ in range(N)]

result = bfs(N, M, K, grid)

print(result)