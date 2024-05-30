N = int(input())

maxPrice = 0
for _ in range(N):
    dice = list(map(int, input().split()))
    cntDice = [[1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0]]
    for d in dice:
        cntDice[d-1][1] += 1
        
    cntDice.sort(key=lambda x:(-x[1], -x[0]))
    
    maxDice = cntDice[0]
    secondDice = cntDice[1]
    minDice = cntDice[-1]
    
    if maxDice[1] == 4:      
        maxPrice = max(maxPrice, 50000 + maxDice[0] * 5000)
    elif maxDice[1] == 3:
        maxPrice = max(maxPrice, 10000 + maxDice[0] * 1000)
    elif maxDice[1] == 2:
        if secondDice[1] == 2:
            maxPrice = max(maxPrice, 2000 + maxDice[0] * 500 + secondDice[0] * 500)
        else:
            maxPrice = max(maxPrice, 1000 + maxDice[0] * 100)
    else:
        maxPrice = max(maxPrice, maxDice[0] * 100)

print(maxPrice)