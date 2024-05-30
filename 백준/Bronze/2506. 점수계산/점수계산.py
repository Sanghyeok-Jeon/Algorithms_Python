N = int(input())
nowScore = 0
totalScore = 0
for s in map(int, input().split()):
    if s:
        if nowScore:
            nowScore += 1
        else:
            nowScore = 1
        totalScore += nowScore
    else:
        nowScore = 0
print(totalScore)