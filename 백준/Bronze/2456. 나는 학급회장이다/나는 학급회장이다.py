N = int(input())
score = [0, 0, 0]
scoreSquare = [0, 0, 0]

for n in range(N):
    s1, s2, s3 = map(int, input().split())

    score[0] += s1
    score[1] += s2
    score[2] += s3
    scoreSquare[0] += s1 * s1
    scoreSquare[1] += s2 * s2
    scoreSquare[2] += s3 * s3

maxScore = max(score)
if score.count(maxScore) > 1:
    maxScoreSquare = max(scoreSquare)
    idx = scoreSquare.index(maxScoreSquare)

    if scoreSquare.count(maxScoreSquare) > 1:
        print(0, maxScore)
    else:
        print(idx+1, maxScore)
else:
    print(score.index(maxScore)+1, maxScore)