p, m = map(int, input().split())
rooms = []

for _ in range(p):
    l, n = input().split()
    l = int(l)

    # 개설된 방이 있는 경우
    if len(rooms):
        room_made = False
        # 개설된 방들을 탐색
        for i in range(len(rooms)):
            # 플레이어 레벨이 처음 입장한 플레이어의 레벨을 기준으로 -10 ~ +10 사이에 포함되는 경우
            if rooms[i][0][0] - 10 <= l <= rooms[i][0][0] + 10:
                # 현재 보는 방의 정원이 초과 되지 않은 경우
                if len(rooms[i]) < m:
                    rooms[i].append([l, n])
                    room_made = True
                    break
                # 초과된 경우
                else:
                    continue

        # 개설된 방에 입장할 곳이 없는 경우
        if not room_made:
            rooms.append([[l, n]])
    # 개설된 방이 하나도 없는 경우
    else:
        rooms.append([[l, n]])

for room in rooms:
    room.sort(key=lambda x: x[1])

    if len(room) == m:
        print('Started!')
    else:
        print('Waiting!')

    for lv, nm in room:
        print(lv, nm)