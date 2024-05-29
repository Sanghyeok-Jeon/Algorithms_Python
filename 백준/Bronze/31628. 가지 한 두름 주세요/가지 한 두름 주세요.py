eggplants = [list(input().split()) for _ in range(10)]

cnt_durm = 0

for i in range(10):
    possible_durm = True
    for j in range(1, 10):
        if eggplants[i][j-1] != eggplants[i][j]:
            possible_durm = False
            break

    if possible_durm:
        cnt_durm += 1

for j in range(10):
    possible_durm = True
    for i in range(1, 10):
        if eggplants[i-1][j] != eggplants[i][j]:
            possible_durm = False
            break

    if possible_durm:
        cnt_durm += 1

print(1 if cnt_durm else 0)