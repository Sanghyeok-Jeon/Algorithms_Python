score = []
for i in range(1, 9):
    score.append((i, int(input())))

score.sort(key=lambda x:-x[1])

total = 0
player = []
for i in range(5):
    total += score[i][1]
    player.append(score[i][0])

print(total)
print(*sorted(player))