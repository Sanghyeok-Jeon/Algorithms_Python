N, a, b = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(N)]
target = X[a-1][b-1]

handsome = 1
if max(X[a-1]) != target:
    handsome = 0
for i in range(N):
    if X[i][b-1] > target:
        handsome = 0
        break

print('ANGRY' if not handsome else 'HAPPY')