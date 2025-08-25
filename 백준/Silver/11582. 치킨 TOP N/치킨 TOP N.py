N = int(input())
score_taste = list(map(int, input().split()))
k = int(input())

step = N // k
for i in range(0, N, step):
    part = score_taste[i:i + step]
    part_sorted = sorted(part)
    score_taste[i:i + step] = part_sorted

print(*score_taste)