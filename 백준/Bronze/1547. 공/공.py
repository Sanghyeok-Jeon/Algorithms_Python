ball = 1
M = int(input())
for _ in range(M):
    X, Y = map(int, input().split())

    if ball == X:
        ball = Y
    elif ball == Y:
        ball = X
print(ball)