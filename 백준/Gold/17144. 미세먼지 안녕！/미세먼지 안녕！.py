def spread_dust(R, C, room):
    # 상하좌우 4방향
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 미세먼지 확산
    new_room = [[0]*C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if room[i][j] > 0: # 미세먼지가 있는 경우
                spread_amount = room[i][j] // 5 # 4방향으로 흩어지는 먼지양
                count = 0 # 확산된 방향의 개수
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < R and 0 <= ny < C and room[nx][ny] != -1:
                        new_room[nx][ny] += spread_amount
                        count += 1

                new_room[i][j] += room[i][j] - (spread_amount * count)

    # 확산된 미세먼지를 기존 방에 업데이트
    for i in range(R):
        for j in range(C):
            room[i][j] = new_room[i][j]

    return room

def move_air(R, C, room, air_cleaner):
    # 위쪽 공기청정기
    x, y = air_cleaner[0]
    dx = [-1, 0, 1, 0] # 바람방향과 역순으로 동작 : 위, 오른쪽, 아래, 왼쪽 순
    dy = [0, 1, 0, -1]
    d = 0 # 현재 방향
    room[x][y] = -1 # 공기청정기 위치 표시

    x += dx[d]
    y += dy[d]
    while True:
        nx = x + dx[d]
        ny = y + dy[d]

        if nx < 0 or nx > air_cleaner[0][0] or ny < 0 or ny >= C: # 범위를 벗어나면 방향 전환
            d = (d + 1) % 4
            nx = x + dx[d]
            ny = y + dy[d]

        if room[nx][ny] == -1: # 공기청정기를 만나면 종료
            room[x][y] = 0
            break

        room[x][y] = room[nx][ny] # 값 업데이트
        x, y = nx, ny

    # 아래쪽 공기청정기
    x, y = air_cleaner[1]
    dx = [1, 0, -1, 0] # 바람방향과 역순으로 동작 : 아래, 오른쪽, 위, 왼쪽 순
    dy = [0, 1, 0, -1]
    d = 0
    room[x][y] = -1 # 공기청정기 위치 표시

    x += dx[d]
    y += dy[d]
    while True:
        nx = x + dx[d]
        ny = y + dy[d]

        if nx < air_cleaner[1][0] or nx >= R or ny < 0 or ny >= C: # 범위 벗어나면 방향 전환
            d = (d + 1) % 4
            nx = x + dx[d]
            ny = y + dy[d]

        if room[nx][ny] == -1: # 공기청정기 만나면 종료
            room[x][y] = 0
            break

        room[x][y] = room[nx][ny] # 값 업데이트
        x, y = nx, ny

    return room

def total_dust(R, C, T, room, air_cleaner):
    for _ in range(T):
        # 새로운 방 상태 업데이트
        room = spread_dust(R, C, room)
        # 공기청정기 작동
        room = move_air(R, C, room, air_cleaner)

    # 남은 미세먼지 양 계산
    total_dust = 0
    for i in range(R):
        for j in range(C):
            if room[i][j] > 0:
                total_dust += room[i][j]

    return total_dust

R, C, T = map(int, input().split())
room = []
air_cleaner = []
for i in range(R):
    row = list(map(int, input().split()))
    room.append(row)
    if row[0] == -1: # 공기청정기 위치 저장
        air_cleaner.append((i, 0))

result = total_dust(R, C, T, room, air_cleaner)
print(result)