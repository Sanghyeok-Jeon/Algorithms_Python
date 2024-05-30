from collections import deque

def air_find(x, y):
    q = deque()
    q.append((x, y))
    data[x][y] = -1    # 이미 탐색한 공기는 -1
    while q:
        i, j = q.popleft()
        for mode in range(4):
            ni = i + di[mode]
            nj = j + dj[mode]
            if 0 <= ni < N and 0 <= nj < M:
                if data[ni][nj] == -1:   # 이미 탐색한 공기는 지나감
                    continue
                elif data[ni][nj] == 1:  # 1변이 닿은 치즈는 2
                    data[ni][nj] = 2
                elif data[ni][nj] == 2:  # 2변 이상 닿은 치즈는 3
                    data[ni][nj] = 3
                elif data[ni][nj] == 0:  # 새로운 공기인 경우 -1로 변경후 데크에 넣음
                    data[ni][nj] = -1
                    q.append((ni, nj))

def melting():
    cnt = 0
    for i in range(N):
        for j in range(M):
            # 공기인 경우 0으로 초기화
            if data[i][j] == -1:
                data[i][j] = 0
            # 한 변만 공기에 접촉한 치즈의 경우 1로 초기화
            elif data[i][j] == 2:
                data[i][j] = 1
            # 2변 이상 공기에 닿은 치즈는 녹이고 0으로 초기화
            elif data[i][j] == 3:
                cnt += 1
                data[i][j] = 0

    return cnt

N, M = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]
time = 0

# 오른쪽, 아래, 왼쪽, 위쪽 방향
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

while True:
    # 공기가 접하는 면 개수 구하는 함수
    air_find(0, 0)

    # 녹은 치즈가 있는지 확인
    if not melting():
        break

    # 1시간 추가
    time += 1

print(time)
