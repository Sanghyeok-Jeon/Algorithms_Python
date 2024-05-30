from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    check_d = [[0] * M for _ in range(N)]    # 방문 체크 및 거리 계산을 위한 리스트
    check_d[x][y] = 1    # 시작점 방문 체크
    max_value = 0

    while q:
        x, y = q.popleft()
        for mode in range(4):
            nx = x + dx[mode]
            ny = y + dy[mode]
            if 0 <= nx < N and 0 <= ny < M:
                if treasure_map[nx][ny] == 'L' and check_d[nx][ny] == 0:     # 아직 방문하지 않은 땅이라면
                    q.append((nx, ny))
                    check_d[nx][ny] = check_d[x][y] + 1
                    max_value = max(max_value, check_d[nx][ny])    # 최대 거리 갱신

    return max_value - 1    # 최대 거리 반환 (시작점 1 차감)

N, M = map(int, input().split())
treasure_map = [list(input()) for _ in range(N)]    # 보물섬 지도
result = 0

for i in range(N):
    for j in range(M):
        if treasure_map[i][j] == 'L':    # 땅인 경우
            result = max(result, bfs(i, j))

print(result)