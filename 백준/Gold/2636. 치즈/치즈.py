from collections import deque

def air_bfs(x, y, count):
    q = deque()
    q.append((x, y))

    visited = [[0] * M for _ in range(N)]
    visited[x][y] = 1

    while q:
        i, j = q.popleft()
        for mode in range(4):
            ni = i + di[mode]
            nj = j + dj[mode]

            if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj]:
                visited[ni][nj] = 1
                # 치즈인 경우
                if data[ni][nj] == 1:
                    data[ni][nj] = -1
                    count -= 1
                # 공기인 경우
                else:
                    q.append((ni, nj))

    return count

def melting():
    for i in range(N):
        for j in range(M):
            if data[i][j] == -1:
                data[i][j] = 0

N, M = map(int, input().split())
data = []
cheese_cnt = 0
for _ in range(N):
    d = list(map(int, input().split()))
    cheese_cnt += sum(d)
    data.append(d)

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

time = 0
last_cheese = cheese_cnt
while cheese_cnt:
    # 한 차례 녹고 남은 치즈 개수 
    cheese_cnt = air_bfs(0, 0, cheese_cnt)

    if cheese_cnt:
        last_cheese = cheese_cnt

    time += 1
    
    # 치즈 녹이기
    melting()

print(time)
print(last_cheese)