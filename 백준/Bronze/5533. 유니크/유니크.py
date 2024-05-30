N = int(input())
playerNumbers = [list(map(int, input().split())) for _ in range(N)]
scores = [0] * N

for nthNumber in zip(*playerNumbers):
    for n, score in enumerate(nthNumber):
        if nthNumber.count(score) == 1:
            scores[n] += score

for score in scores:
    print(score)