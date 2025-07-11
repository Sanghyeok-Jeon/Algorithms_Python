from itertools import combinations

N, M = map(int, input().split())
favorite = [list(map(int, input().split())) for _ in range(N)]

maxSum = 0
for a, b, c in combinations(range(M), 3):
    tmpSum = 0
    for i in range(N):
        tmpSum += max(favorite[i][a], favorite[i][b], favorite[i][c])
    maxSum = max(maxSum, tmpSum)

print(maxSum)