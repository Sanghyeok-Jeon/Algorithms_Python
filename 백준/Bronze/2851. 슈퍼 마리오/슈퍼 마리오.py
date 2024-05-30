mushrooms = [int(input()) for _ in range(10)]

score = 0
for mr in mushrooms:
    score += mr
    if score >= 100:
        if score - 100 > 100 - (score - mr):
            score -= mr
        break

print(score)