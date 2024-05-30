import sys
from collections import deque
input = sys.stdin.readline

# 그룹 내 0의 개수를 찾는 함수
def BFS(start, groupNo):
    q = deque()
    q.append(start)

    cnt = 1
    while q:
        x, y = q.popleft()
        zeroGroups[x][y] = groupNo

        for mode in range(4):
            nx = x + dx[mode]
            ny = y + dy[mode]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and not walls[nx][ny]:
                visited[nx][ny] = 1
                q.append((nx, ny))
                cnt += 1

    return cnt

N, M = map(int, input().split())
walls = [list(map(int, input().strip())) for _ in range(N)]    # 벽의 위치
visited = [[0] * M for _ in range(N)]
zeroGroups = [[0] * M for _ in range(N)]    # 0으로 이루어진 그룹들 - 발견 순서대로 임의로 번호 매김
zeroGroupCnt = {0: 0}    # 각 그룹별 0의 개수

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 각 그룹별 0의 개수를 찾는 BFS 알고리즘
groupNo = 1
for i in range(N):
    for j in range(M):
        if not walls[i][j] and not visited[i][j]:
            visited[i][j] = 1
            zeroCnt = BFS((i, j), groupNo)
            zeroGroupCnt[groupNo] = zeroCnt
            groupNo += 1

# 벽을 제거했을 때의 이동가능한 칸의 수
for x in range(N):
    for y in range(M):
        if walls[x][y]:
            zeroGroupList = set()
            for mode in range(4):
                nx = x + dx[mode]
                ny = y + dy[mode]
                if 0 <= nx < N and 0 <= ny < M:
                    zeroGroupList.add(zeroGroups[nx][ny])

            for zeroGroup in zeroGroupList:
                walls[x][y] += zeroGroupCnt[zeroGroup]    # 벽이 없어진 공간도 이동할 수 있는 곳이니 벽을 표현했던 1에 그대로 더해줌
                walls[x][y] %= 10

for w in walls:
    print(''.join(map(str, w)))