cardA = list(map(int, input().split()))
cardB = list(map(int, input().split()))

scoreA, scoreB = 0, 0
winner = 'D'
for i in range(10):
    if cardA[i] > cardB[i]:
        scoreA += 3
        winner = 'A'
    elif cardA[i] < cardB[i]:
        scoreB += 3
        winner = 'B'
    else:
        scoreA += 1
        scoreB += 1
    
print(scoreA, scoreB)
if scoreA > scoreB:
    print('A')
elif scoreA < scoreB:
    print('B')
else:
    print(winner)