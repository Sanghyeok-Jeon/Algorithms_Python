winner = -1
score = 0
for i in range(1, 6):
    tmpWinner = i
    tmpScore = sum(map(int, input().split()))

    if tmpScore > score:
        score = tmpScore
        winner = tmpWinner

print(winner, score)