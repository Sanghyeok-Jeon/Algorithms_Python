A, B, C, X, Y = map(int, input().split())
cost = 0

if A+B < 2*C:
    cost += A*X + B*Y
else:
    cost += 2 * C * min(X, Y)
    if X >= Y:
        diff = X - Y
        cost += min(A*diff, 2*C*diff)
    else:
        diff = Y - X
        cost += min(B*diff, 2*C*diff)

print(cost)