K = int(input())
N = int(input())
lst_result = [tuple(input().split()) for i in range(N)]

passtime = 210
idx = 0
player = K
while True:
    time, answer = lst_result[idx]

    passtime -= int(time)

    if passtime < 0:
        print(player)
        break

    if answer == 'T':
        player += 1
        if player > 8:
            player = 1

    idx += 1