score = list(map(int, input().split()))
maxScore = [100, 100, 200, 200, 300, 300, 400, 400, 500]
total = 0
result = 'none'
for i in range(9):
    if score[i] > maxScore[i]:
        result = 'hacker'
        break
    else:
        total += score[i]

if total >= 100:
    result = 'draw'

print(result)