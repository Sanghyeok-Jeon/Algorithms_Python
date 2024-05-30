n = int(input())
scoreCy, scoreSd = 100, 100
for _ in range(n):
    cy, sd = map(int, input().split())
    if cy > sd:
        scoreSd -= cy
    elif cy < sd:
        scoreCy -= sd

print(scoreCy)
print(scoreSd)