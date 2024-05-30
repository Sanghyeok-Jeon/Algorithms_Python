dice = [[i, 0] for i in range(7)]
maxDice = 0
for d in map(int, input().split()):
    maxDice = max(d, maxDice)
    dice[int(d)][1] += 1

dice.sort(key= lambda x: (-x[1], -x[0]))
target = dice[0]
price = 0
if target[1] == 1:
    price += 100*target[0]
elif target[1] == 2:
    price += 1000 + 100*target[0]
else:
    price += 10000 + 1000*target[0]

print(price)