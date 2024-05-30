from collections import deque

def BFS(x, y, wall):
    q = deque()
    q.append(((x, y, wall)))  # 벽 부수지 않은 상태로 시작
    visited[x][y][wall] = 1

    while q:
        i, j, w = q.popleft()

        # 도착점에 도달한 경우 최단 거리 출력
        if i == N-1 and j == M-1:
            return visited[i][j][w]

        # 상하좌우 이동
        for mode in range(4):
            ni = i + di[mode]
            nj = j + dj[mode]

            if 0 <= ni < N and 0 <= nj < M:
                # 벽을 부수지 않고 이동하는 경우
                if maze[ni][nj] == 0 and visited[ni][nj][w] == 0:
                    visited[ni][nj][w] = visited[i][j][w] + 1
                    q.append((ni, nj, w))
            
                # 벽을 부수고 이동하는 경우
                if maze[ni][nj] == 1 and w == 0:
                    visited[ni][nj][1] = visited[i][j][0] + 1
                    q.append((ni, nj, 1))

    return -1  # 도착점에 도달하지 못한 경우

N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]

# 상하좌우 이동
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

visited = [[[0]*2 for _ in range(M)] for _ in range(N)]

print(BFS(0, 0, 0))